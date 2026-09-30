# FOLIO argument base for Seqprover

A curated base of formalised first-order-logic arguments for the research
studies in the course *Intelektualiosios sistemos* (VU MIF, autumn 2026):
testing how well a non-logic-based AI system decides whether a conclusion
follows from a set of premises, with every answer checked by a
sequent-calculus prover.

- **Arguments:** 60, taken from FOLIO (see Source). Nothing here is
  self-formalised. Labels are balanced: 20 *True*, 20 *False*, 20 *Uncertain*.
- **Premise counts:** 50 of the 60 arguments have 5 or more premises
  (course requirement: at least 10). They come from 24 different FOLIO stories.
- **Formats:** natural language (English), the original FOLIO first-order
  formulas, and machine-checkable [Seqprover](https://cspsat.gitlab.io/seqprover/)
  sequents.

| File | Contents |
|---|---|
| `arguments.md` | Human-readable list: premises, conclusion, FOL, Seqprover sequent |
| `arguments.json` | The same data as records, plus selection statistics |
| `sequents/ARG-NN.goal.pl` | Seqprover batch input: premises `-->` conclusion |
| `sequents/ARG-NN.neg.pl` | Seqprover batch input: premises `-->` ¬conclusion |
| `proofs/` | Prover output (proof trees or "Fail to prove") for every sequent |
| `results.md`, `results.json` | Prover verdicts compared with the FOLIO labels |
| `exclusions.json` | Every validation-set row that was *not* usable, with the reason |
| `scripts/folio2seq.py` | FOL → Seqprover translator and subset selection |
| `scripts/run_seqprover.py` | Runs all sequents through Seqprover and writes the results |
| `seqprover/` | Vendored `seqprover.pl` (N. Tamura, v2.0) and its user guide |

## Source

**FOLIO: Natural Language Reasoning with First-Order Logic.**
Simeng Han, Hailey Schoelkopf, Yilun Zhao, Zhenting Qi, Martin Riddell,
Wenfei Zhou, James Coady, David Peng, Yujie Qiao, Luke Benson, Lucy Sun,
Alex Wardle-Solano, Hannah Szabo, Ekaterina Zubova, Matthew Burtell,
Jonathan Fan, Yixin Liu, Brian Wong, Malcolm Sailor, Ansong Ni, Linyong Nan,
Jungo Kasai, Tao Yu, Rui Zhang, Alexander R. Fabbri, Wojciech Kryscinski,
Semih Yavuz, Ye Liu, Xi Victoria Lin, Shafiq Joty, Yingbo Zhou,
Caiming Xiong, Rex Ying, Arman Cohan, Dragomir Radev.
EMNLP 2024 (first released 2022). arXiv:2209.00840.

- Dataset (v2, MIT licence): <https://huggingface.co/datasets/yale-nlp/FOLIO>
- Original release and code: <https://github.com/Yale-LILY/FOLIO>

FOLIO has 1,430 human-written examples over 487 premise sets. Each example
is a set of English premises with a conclusion, hand-annotated in
first-order logic and labelled *True* (the conclusion follows), *False*
(its negation follows) or *Uncertain* (neither follows). This repository
uses the **validation split of FOLIO v2** (203 examples).

## How the 60 were chosen

`scripts/folio2seq.py build` is deterministic. It

1. parses every FOL formula with the standard precedence
   (¬ > ∧ > ∨ > →, quantifier scopes over the next unit);
2. drops rows Seqprover cannot express or that are malformed in FOLIO:
   `⊕` (exclusive or), `↔`, `=` (identity), unbalanced parentheses,
   free variables, and a predicate used with two different arities in the
   same story. One further row (FOLIO example 1414) is excluded by hand because
   its FOL conclusion omits the negation that the English conclusion has, so
   the prover proves the opposite of the label. Reasons are listed per row in
   `exclusions.json`;
3. for each label, takes examples in `example_id` order, preferring those
   with ≥ 5 premises and at most 3 examples per FOLIO story, and tops up
   with shorter examples until it has 20 per label.

Rebuild from the source file (needs a Hugging Face login for the download):

```
hf download yale-nlp/FOLIO --repo-type=dataset --local-dir data
python3 scripts/folio2seq.py build --source data/folio_v2_validation.jsonl --out .
```

## Seqprover translation

Seqprover reads Prolog terms, so the translator emits fully parenthesised
formulas with these conventions:

| FOLIO | Seqprover |
|---|---|
| `¬F` | `~F` |
| `F ∧ G`, `F ∨ G`, `F → G` | `(F/\G)`, `(F\/G)`, `(F->G)` |
| `∀x F`, `∃x F` | `X@(F)`, `X#(F)` |
| predicate `Student(x)` | `student(X)` (initial lowercased; variables uppercased) |
| constant `mia`, `1984` | unchanged |
| constant `2024UnitedStatesElection`, `świątek` | quoted: `'2024UnitedStatesElection'` |

For every argument two sequents are produced. `premises --> conclusion` must
be derivable exactly when the label is *True*; `premises --> ~conclusion`
exactly when the label is *False*; for *Uncertain* neither is derivable.

Run the prover on all sequents (needs SWI-Prolog, `brew install swi-prolog`):

```
python3 scripts/run_seqprover.py --threshold 5 --timeout 120
```

Seqprover limits the number of L∀ / R∃ (and cut / contraction) rule
applications per proof path to `threshold`. First-order derivability is
undecidable, so "Fail to prove" at a given threshold is not a proof of
non-derivability; for *True* and *False* arguments a failure means the
threshold is too low. Proofs are usually found in milliseconds, but showing
that a sequent is *not* derivable means exhausting the whole search space up
to the threshold, which for arguments with several universally quantified
premises often exceeds the per-sequent timeout. `results.md` therefore
distinguishes `proved`, `not_proved` (search exhausted) and `timeout`. The
FOLIO label remains the ground truth for the study; the prover output is the
independent check, and `proofs/` holds the proof trees for the appendix.

Tokenising details that matter when writing sequents by hand: Prolog glues
adjacent symbol characters into one token, so `->~p` is a syntax error and
must be written `-> ~p`; likewise `~~p` must be `~ ~p`.

## Tests

```
python3 -m pytest -q tests
```

## Licences

FOLIO is released under the MIT licence by its authors; the excerpts here are
redistributed with attribution. `seqprover.pl` is by Naoyuki Tamura (Kobe
University) and may be freely distributed and modified per its header.
Everything else in this repository is MIT.
