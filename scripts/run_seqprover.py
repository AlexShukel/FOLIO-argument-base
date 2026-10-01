#!/usr/bin/env python3
"""Run every sequent in sequents/ through Seqprover (SWI-Prolog batch mode),
store the proof output in proofs/, and compare with the FOLIO label.

    run_seqprover.py --threshold 5 --timeout 120 [--only ARG-01,ARG-02]

Seqprover caps the number of L∀ / R∃ / cut / contraction rule applications per
proof path at `threshold` (default 5 in the prover). A valid argument that
needs more instantiations is reported as "not proved", so a mismatch on a
True/False argument usually means the threshold must go up, not that FOLIO is
wrong. Results are written to results.json and results.md.
"""
from __future__ import annotations

import argparse
import os
from concurrent.futures import ThreadPoolExecutor
import json
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROVER = ROOT / "seqprover" / "seqprover.pl"


def run_one(seq_file: Path, threshold: int, timeout: int) -> dict:
    goal = f"set_threshold({threshold}),batch"
    t0 = time.time()
    try:
        p = subprocess.run(
            ["swipl", "-q", "-g", goal, str(PROVER)],
            stdin=seq_file.open("rb"), capture_output=True, timeout=timeout,
        )
        out = p.stdout.decode("utf-8", "replace") + p.stderr.decode("utf-8", "replace")
        status = "timeout"
        if "# END Proof" in out:
            status = "proved"
        elif "# Fail to prove" in out:
            status = "not_proved"
        elif "# Syntax error" in out or "rror" in out:
            status = "error"
    except subprocess.TimeoutExpired as e:
        out = (e.stdout or b"").decode("utf-8", "replace") + "\n# TIMEOUT\n"
        status = "timeout"
    m = re.search(r"# Proved in (\d+) msec", out)
    return {"status": status, "seconds": round(time.time() - t0, 2),
            "prover_msec": int(m.group(1)) if m else None, "output": out}


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--threshold", type=int, default=5)
    ap.add_argument("--timeout", type=int, default=120, help="seconds per sequent")
    ap.add_argument("--only", default="", help="comma-separated ARG ids")
    ap.add_argument("--arguments", default=str(ROOT / "arguments.json"))
    ap.add_argument("--jobs", type=int, default=max(1, (os.cpu_count() or 2) - 1),
                    help="parallel swipl processes")
    ap.add_argument("--resume", action="store_true",
                    help="reuse proofs/*.txt that already ended in proved / not_proved; rerun the rest")
    args = ap.parse_args(argv)

    if not shutil.which("swipl"):
        sys.exit("swipl not found: brew install swi-prolog")
    data = json.loads(Path(args.arguments).read_text("utf-8"))
    only = {x.strip() for x in args.only.split(",") if x.strip()}
    proofs = ROOT / "proofs"
    proofs.mkdir(exist_ok=True)

    selected = [a for a in data["arguments"] if not only or a["id"] in only]
    jobs = [(a["id"], kind, suffix) for a in selected for kind, suffix in (("goal", "goal"), ("negated_goal", "neg"))]

    def work(job):
        arg_id, kind, suffix = job
        done = proofs / f"{arg_id}.{suffix}.txt"
        if args.resume and done.exists():
            prev = done.read_text("utf-8", "replace")
            if "# END Proof" in prev or "# Fail to prove" in prev:
                m = re.search(r"# Proved in (\d+) msec", prev)
                r = {"status": "proved" if "# END Proof" in prev else "not_proved", "seconds": 0.0,
                     "prover_msec": int(m.group(1)) if m else None}
                print(f"  {arg_id}.{suffix}: {r['status']} (reused)", flush=True)
                return job, r
        r = run_one(ROOT / "sequents" / f"{arg_id}.{suffix}.pl", args.threshold, args.timeout)
        (proofs / f"{arg_id}.{suffix}.txt").write_text(r.pop("output"), "utf-8")
        print(f"  {arg_id}.{suffix}: {r['status']} ({r['seconds']}s)", flush=True)
        return job, r

    with ThreadPoolExecutor(max_workers=args.jobs) as pool:
        outcomes = dict((job, r) for job, r in pool.map(work, jobs))

    results = []
    for arg in selected:
        rec = {"id": arg["id"], "label": arg["label"], "expected": arg["seqprover"]["expected"], "runs": {}}
        for kind, suffix in (("goal", "goal"), ("negated_goal", "neg")):
            rec["runs"][kind] = outcomes[(arg["id"], kind, suffix)]
        got = {k: v["status"] for k, v in rec["runs"].items()}
        exp = rec["expected"]
        rec["agrees"] = all(
            (got[k] == "proved") == exp[k] for k in ("goal", "negated_goal")
        ) and "timeout" not in got.values() and "error" not in got.values()
        results.append(rec)
        print(f"{arg['id']} {arg['label']:9s} goal={got['goal']:10s} neg={got['negated_goal']:10s} "
              f"{'OK' if rec['agrees'] else 'MISMATCH'}", flush=True)

    summary = {
        "threshold": args.threshold, "timeout": args.timeout, "n": len(results),
        "agree": sum(r["agrees"] for r in results),
        "mismatch_ids": [r["id"] for r in results if not r["agrees"]],
    }
    Path(ROOT / "results.json").write_text(json.dumps({"summary": summary, "results": results}, indent=2) + "\n", "utf-8")
    md = [f"# Seqprover results (threshold {args.threshold}, timeout {args.timeout}s)", "",
          f"{summary['agree']} / {summary['n']} arguments agree with the FOLIO label.", "",
          "| ID | Label | goal | ¬goal | Agrees | prover ms (goal / ¬goal) |", "|---|---|---|---|---|---|"]
    for r in results:
        g, n = r["runs"]["goal"], r["runs"]["negated_goal"]
        md.append(f"| {r['id']} | {r['label']} | {g['status']} | {n['status']} | {'yes' if r['agrees'] else 'NO'} | "
                  f"{g['prover_msec'] if g['prover_msec'] is not None else '-'} / {n['prover_msec'] if n['prover_msec'] is not None else '-'} |")
    Path(ROOT / "results.md").write_text("\n".join(md) + "\n", "utf-8")
    print(json.dumps(summary))
    return 0


if __name__ == "__main__":
    sys.exit(main())
