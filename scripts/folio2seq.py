#!/usr/bin/env python3
"""Convert FOLIO first-order-logic annotations into Seqprover sequents and
select a curated argument base.

Library use:
    fol_to_seqprover("∀x (Student(x) → Smart(x))")  ->  "X@((student(X) -> smart(X)))"
    sequent_for(premises_fol, conclusion_fol, label) -> {goal, negated_goal, expected}

CLI use:
    folio2seq.py build --source data/folio_v2_validation.jsonl data/folio_v2_train.jsonl --labels True,False --per-label 30 --out .

FOLIO precedence assumed: ¬ > ∧ > ∨ > →, quantifier scopes over the next unit.
Seqprover (Tamura) gives /\\ and \\/ equal precedence, so the output is
fully parenthesised. Unsupported input (⊕, ↔, =, free variables) raises
ConvertError so that such rows can be excluded with a reason.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterator, Union

# ----------------------------------------------------------------------------
# Errors and AST
# ----------------------------------------------------------------------------


class ConvertError(ValueError):
    """Raised when a formula cannot be expressed in Seqprover syntax."""


@dataclass(frozen=True)
class Pred:
    name: str
    args: tuple[str, ...]


@dataclass(frozen=True)
class Not:
    f: "Node"


@dataclass(frozen=True)
class Bin:
    op: str  # 'and' | 'or' | 'imp'
    a: "Node"
    b: "Node"


@dataclass(frozen=True)
class Quant:
    kind: str  # 'all' | 'ex'
    var: str
    body: "Node"


Node = Union[Pred, Not, Bin, Quant]

# ----------------------------------------------------------------------------
# Tokenizer
# ----------------------------------------------------------------------------

UNSUPPORTED = {"⊕": "xor", "↔": "iff", "⟷": "iff", "=": "equality", "≠": "equality",
               "⊃": "alt-implication", "∼": "alt-negation"}

_TOKEN_RE = re.compile(
    r"\s+|(?P<all>∀)|(?P<ex>∃)|(?P<not>¬)|(?P<and>∧)|(?P<or>∨)|(?P<imp>→)"
    r"|(?P<lp>\()|(?P<rp>\))|(?P<comma>,)|(?P<ident>[^\W](?:\w|-(?=\w))*)"  # Unicode-aware; inner hyphens allowed
)


@dataclass
class Tok:
    kind: str
    text: str
    pos: int


def tokenize(fol: str) -> list[Tok]:
    toks: list[Tok] = []
    i = 0
    while i < len(fol):
        ch = fol[i]
        if ch in UNSUPPORTED:
            raise ConvertError(f"unsupported connective {ch!r} ({UNSUPPORTED[ch]}) at {i}")
        m = _TOKEN_RE.match(fol, i)
        if not m:
            raise ConvertError(f"unexpected character {ch!r} at {i} in {fol!r}")
        i = m.end()
        if m.lastgroup is None:  # whitespace
            continue
        toks.append(Tok(m.lastgroup, m.group(m.lastgroup), m.start()))
    return toks


# ----------------------------------------------------------------------------
# Parser (recursive descent)
#   imp  := or ( '→' imp )?          right associative
#   or   := and ( '∨' and )*         right associative in output
#   and  := unary ( '∧' unary )*
#   unary:= '¬' unary | ('∀'|'∃') var unary | '(' imp ')' | atom
# ----------------------------------------------------------------------------


class _Parser:
    def __init__(self, toks: list[Tok], src: str):
        self.toks = toks
        self.i = 0
        self.src = src

    def peek(self) -> Tok | None:
        return self.toks[self.i] if self.i < len(self.toks) else None

    def take(self, kind: str | None = None) -> Tok:
        t = self.peek()
        if t is None:
            raise ConvertError(f"unexpected end of formula in {self.src!r}")
        if kind and t.kind != kind:
            raise ConvertError(f"expected {kind}, got {t.text!r} at {t.pos} in {self.src!r}")
        self.i += 1
        return t

    def parse(self) -> Node:
        node = self.imp()
        if self.peek() is not None:
            t = self.peek()
            raise ConvertError(f"trailing token {t.text!r} at {t.pos} in {self.src!r}")
        return node

    def imp(self) -> Node:
        left = self.disj()
        t = self.peek()
        if t and t.kind == "imp":
            self.take()
            return Bin("imp", left, self.imp())
        return left

    def _chain(self, kind: str, sub, op: str) -> Node:
        parts = [sub()]
        while (t := self.peek()) and t.kind == kind:
            self.take()
            parts.append(sub())
        node = parts[-1]
        for p in reversed(parts[:-1]):
            node = Bin(op, p, node)
        return node

    def disj(self) -> Node:
        return self._chain("or", self.conj, "or")

    def conj(self) -> Node:
        return self._chain("and", self.unary, "and")

    def unary(self) -> Node:
        t = self.take()
        if t.kind == "not":
            return Not(self.unary())
        if t.kind in ("all", "ex"):
            var = self.take("ident").text
            return Quant(t.kind, var, self.unary())
        if t.kind == "lp":
            node = self.imp()
            self.take("rp")
            return node
        if t.kind == "ident":
            nxt = self.peek()
            if nxt and nxt.kind == "lp":
                self.take("lp")
                args = [self.take("ident").text]
                while (c := self.peek()) and c.kind == "comma":
                    self.take()
                    args.append(self.take("ident").text)
                self.take("rp")
                return Pred(t.text, tuple(args))
            return Pred(t.text, ())
        raise ConvertError(f"unexpected token {t.text!r} at {t.pos} in {self.src!r}")


def parse_fol(fol: str) -> Node:
    return _Parser(tokenize(fol), fol).parse()


# ----------------------------------------------------------------------------
# Emission in Seqprover syntax
# ----------------------------------------------------------------------------

_VARLIKE = re.compile(r"^[u-z]\d*$")          # FOLIO variables: x, y, z (u, v, w reserved), optional digit suffix
_PLAIN_ATOM = re.compile(r"^[a-z][A-Za-z0-9_]*$")
_INTEGER = re.compile(r"^\d+$")


def _atom(name: str) -> str:
    if _PLAIN_ATOM.match(name):
        return name
    if _INTEGER.match(name):
        return name
    return "'" + name.replace("\\", "\\\\").replace("'", "\\'") + "'"


def _pred_name(name: str) -> str:
    lowered = name[0].lower() + name[1:]
    return _atom(lowered)


def _var(name: str) -> str:
    return name[0].upper() + name[1:]


def _emit(node: Node, bound: frozenset[str], src: str) -> str:
    if isinstance(node, Pred):
        args = []
        for a in node.args:
            if a in bound:
                args.append(_var(a))
            elif _VARLIKE.match(a):
                raise ConvertError(f"free variable {a!r} in {src!r}")
            else:
                args.append(_atom(a))
        head = _pred_name(node.name)
        return f"{head}({','.join(args)})" if args else head
    if isinstance(node, Not):
        # Prolog glues adjacent symbol characters into one token ("->~", "~~"),
        # so a space separates a negation from a preceding operator or negation.
        sep = " " if isinstance(node.f, Not) else ""
        return "~" + sep + _emit(node.f, bound, src)
    if isinstance(node, Bin):
        sym = {"and": "/\\", "or": "\\/", "imp": "->"}[node.op]
        return f"({_emit(node.a, bound, src)} {sym} {_emit(node.b, bound, src)})"
    if isinstance(node, Quant):
        sym = "@" if node.kind == "all" else "#"
        inner = _emit(node.body, bound | {node.var}, src)
        return f"{_var(node.var)}{sym}({inner})"
    raise TypeError(node)


def fol_to_seqprover(fol: str) -> str:
    """Translate one closed FOLIO formula into Seqprover syntax."""
    return _emit(parse_fol(fol), frozenset(), fol)


def predicate_arities(node: Node) -> Iterator[tuple[str, int]]:
    if isinstance(node, Pred):
        yield node.name, len(node.args)
    elif isinstance(node, Not):
        yield from predicate_arities(node.f)
    elif isinstance(node, Bin):
        yield from predicate_arities(node.a)
        yield from predicate_arities(node.b)
    elif isinstance(node, Quant):
        yield from predicate_arities(node.body)


# ----------------------------------------------------------------------------
# Sequents
# ----------------------------------------------------------------------------

EXPECTED = {
    # label -> (goal sequent provable?, negated-goal sequent provable?)
    "True": {"goal": True, "negated_goal": False},
    "False": {"goal": False, "negated_goal": True},
    "Uncertain": {"goal": False, "negated_goal": False},
    "Unknown": {"goal": False, "negated_goal": False},
}


def sequent_for(premises_fol: list[str], conclusion_fol: str, label: str) -> dict:
    prem = [fol_to_seqprover(p) for p in premises_fol]
    concl = fol_to_seqprover(conclusion_fol)
    left = ", ".join(prem) if prem else "[]"
    neg = ("~ " if concl.startswith("~") else "~") + concl  # avoid the Prolog token "~~"
    return {
        "goal": f"{left} --> {concl}",
        "negated_goal": f"{left} --> {neg}",
        "expected": EXPECTED[label],
    }


def seqprover_term(sequent: str, output: str = "pretty") -> str:
    """Batch-mode input for `swipl -g batch seqprover.pl`: output form, then sequent."""
    return f"{output}.\n{sequent}.\n"


# ----------------------------------------------------------------------------
# Building the curated base
# ----------------------------------------------------------------------------


def _split(block: str | list[str]) -> list[str]:
    if isinstance(block, list):
        return [x.strip() for x in block if x.strip()]
    return [x.strip() for x in block.split("\n") if x.strip()]


@dataclass
class Candidate:
    example_id: int
    story_id: int
    label: str
    premises: list[str]
    premises_fol: list[str]
    conclusion: str
    conclusion_fol: str
    seq: dict = field(default_factory=dict)
    seq_premises: list[str] = field(default_factory=list)
    seq_conclusion: str = ""
    split: str = ""


def load_rows(path: Path) -> list[dict]:
    return [json.loads(l) for l in path.read_text(encoding="utf-8").splitlines() if l.strip()]


def convert_row(row: dict) -> Candidate:
    prem_nl = _split(row["premises"])
    prem_fol = _split(row["premises-FOL"])
    concl_fol = row["conclusion-FOL"].strip()
    if len(prem_nl) != len(prem_fol):
        raise ConvertError(f"premise count mismatch NL={len(prem_nl)} FOL={len(prem_fol)}")
    trees = [parse_fol(f) for f in prem_fol] + [parse_fol(concl_fol)]
    arities: dict[str, set[int]] = defaultdict(set)
    for t in trees:
        for name, n in predicate_arities(t):
            arities[name].add(n)
    bad = {k: sorted(v) for k, v in arities.items() if len(v) > 1}
    if bad:
        raise ConvertError(f"inconsistent predicate arity {bad}")
    label = row["label"].strip()
    if label not in EXPECTED:
        raise ConvertError(f"unknown label {label!r}")
    seq = sequent_for(prem_fol, concl_fol, label)
    return Candidate(
        example_id=int(row["example_id"]),
        story_id=int(row["story_id"]),
        label="Uncertain" if label == "Unknown" else label,
        premises=prem_nl,
        premises_fol=prem_fol,
        conclusion=row["conclusion"].strip(),
        conclusion_fol=concl_fol,
        seq=seq,
        seq_premises=[fol_to_seqprover(p) for p in prem_fol],
        seq_conclusion=fol_to_seqprover(concl_fol),
    )


def select(cands: list[Candidate], per_label: int, min_premises: int,
           max_per_story: int, labels: tuple[str, ...] = ("True", "False", "Uncertain"),
           split_order: tuple[str, ...] = ()) -> list[Candidate]:
    """Deterministic pick: per label, prefer >= min_premises, cap rows per story,
    then top up with shorter arguments if needed. Candidates are ordered by
    source split (in the order given) and then example_id."""
    rank = {s: i for i, s in enumerate(split_order)}
    chosen: list[Candidate] = []
    story_use: Counter = Counter()
    for label in labels:
        pool = sorted((c for c in cands if c.label == label),
                      key=lambda c: (rank.get(c.split, len(rank)), c.example_id))
        picked: list[Candidate] = []
        for tier in (lambda c: len(c.premises) >= min_premises,
                     lambda c: len(c.premises) < min_premises):
            for c in pool:
                if len(picked) >= per_label:
                    break
                if not tier(c) or story_use[(c.split, c.story_id)] >= max_per_story:
                    continue
                picked.append(c)
                story_use[(c.split, c.story_id)] += 1
        chosen.extend(picked)
    return chosen


def write_outputs(chosen: list[Candidate], excluded: list[dict], out: Path,
                  source_name: str, stats: dict) -> None:
    (out / "sequents").mkdir(parents=True, exist_ok=True)
    records = []
    for i, c in enumerate(chosen, 1):
        arg_id = f"ARG-{i:02d}"
        rec = {
            "id": arg_id,
            "folio_split": c.split,
            "folio_example_id": c.example_id,
            "folio_story_id": c.story_id,
            "label": c.label,
            "n_premises": len(c.premises),
            "premises": c.premises,
            "premises_fol": c.premises_fol,
            "conclusion": c.conclusion,
            "conclusion_fol": c.conclusion_fol,
            "seqprover": {
                "premises": c.seq_premises,
                "conclusion": c.seq_conclusion,
                "goal": c.seq["goal"],
                "negated_goal": c.seq["negated_goal"],
                "expected": c.seq["expected"],
            },
        }
        records.append(rec)
        (out / "sequents" / f"{arg_id}.goal.pl").write_text(seqprover_term(c.seq["goal"]), "utf-8")
        (out / "sequents" / f"{arg_id}.neg.pl").write_text(seqprover_term(c.seq["negated_goal"]), "utf-8")

    (out / "arguments.json").write_text(
        json.dumps({"source": source_name, "stats": stats, "arguments": records},
                   ensure_ascii=False, indent=2) + "\n", "utf-8")
    (out / "exclusions.json").write_text(
        json.dumps(excluded, ensure_ascii=False, indent=2) + "\n", "utf-8")

    md = [f"# Curated FOLIO argument base ({len(records)} arguments)", "",
          f"Source: {source_name}. Labels: True = conclusion follows; "
          "False = negation of the conclusion follows.", ""]
    md.append("| ID | FOLIO split | FOLIO id | Story | Label | Premises |")
    md.append("|---|---|---|---|---|---|")
    for r in records:
        md.append(f"| {r['id']} | {r['folio_split']} | {r['folio_example_id']} | {r['folio_story_id']} | {r['label']} | {r['n_premises']} |")
    md.append("")
    for r in records:
        md += [f"## {r['id']} — {r['label']} (FOLIO {r['folio_split']} example {r['folio_example_id']}, story {r['folio_story_id']})", "",
               "**Premises**", ""]
        for nl, fol in zip(r["premises"], r["premises_fol"]):
            md.append(f"- {nl}  ")
            md.append(f"  `{fol}`")
        md += ["", "**Conclusion**", "", f"- {r['conclusion']}  ", f"  `{r['conclusion_fol']}`", "",
               "**Seqprover**", "", "```", r["seqprover"]["goal"], "```", ""]
    (out / "arguments.md").write_text("\n".join(md), "utf-8")


# FOLIO rows excluded by hand after checking the prover output against the text.
MANUAL_EXCLUSIONS = {
    ("validation", 1414): "FOL conclusion omits the negation present in the natural-language conclusion "
          "('It is not true that ...'); Seqprover proves the un-negated FOL, so the FOL "
          "does not match the label",
}


def build(args: argparse.Namespace) -> int:
    sources = [Path(s) for s in args.source]
    labels = tuple(x.strip() for x in args.labels.split(",") if x.strip())
    cands: list[Candidate] = []
    excluded: list[dict] = []
    n_rows = 0
    for source in sources:
        split = source.stem.replace("folio_v2_", "")
        for row in load_rows(source):
            n_rows += 1
            key = {"split": split, "example_id": row.get("example_id"), "story_id": row.get("story_id"),
                   "label": row.get("label")}
            if (split, int(row["example_id"])) in MANUAL_EXCLUSIONS:
                excluded.append({**key, "reason": "manual: " + MANUAL_EXCLUSIONS[(split, int(row["example_id"]))]})
                continue
            try:
                c = convert_row(row)
                c.split = split
                if c.label in labels:
                    cands.append(c)
                else:
                    excluded.append({**key, "reason": f"label {c.label} not selected"})
            except ConvertError as e:
                excluded.append({**key, "reason": str(e)})
    chosen = select(cands, args.per_label, args.min_premises, args.max_per_story,
                    labels=labels, split_order=tuple(s.stem.replace("folio_v2_", "") for s in sources))
    reasons = Counter(re.split(r"[ {(:]", e["reason"], maxsplit=1)[0] for e in excluded)
    stats = {
        "sources": [s.name for s in sources],
        "labels": list(labels),
        "source_rows": n_rows,
        "convertible_rows": len(cands),
        "excluded_rows": len(excluded),
        "exclusion_reasons": dict(reasons),
        "selected": len(chosen),
        "selected_by_label": dict(Counter(c.label for c in chosen)),
        "selected_by_split": dict(Counter(c.split for c in chosen)),
        "selected_with_min_premises": sum(len(c.premises) >= args.min_premises for c in chosen),
        "selected_stories": len({(c.split, c.story_id) for c in chosen}),
        "min_premises": args.min_premises,
        "max_per_story": args.max_per_story,
    }
    write_outputs(chosen, excluded, Path(args.out), " + ".join(s.name for s in sources), stats)
    print(json.dumps(stats, indent=2))
    return 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    b = sub.add_parser("build", help="select the argument base and write outputs")
    b.add_argument("--source", nargs="+", default=["data/folio_v2_validation.jsonl", "data/folio_v2_train.jsonl"],
                   help="FOLIO jsonl files in priority order")
    b.add_argument("--labels", default="True,False", help="comma-separated labels to include")
    b.add_argument("--out", default=".")
    b.add_argument("--per-label", type=int, default=30)
    b.add_argument("--min-premises", type=int, default=5)
    b.add_argument("--max-per-story", type=int, default=3)
    b.set_defaults(func=build)
    t = sub.add_parser("translate", help="translate one formula given on the command line")
    t.add_argument("formula")
    t.set_defaults(func=lambda a: print(fol_to_seqprover(a.formula)) or 0)
    args = ap.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
