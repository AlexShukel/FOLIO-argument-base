# FOLIO argument base

60 first-order-logic arguments selected from the [FOLIO](https://huggingface.co/datasets/yale-nlp/FOLIO)
dataset (Han et al., 2024, MIT licence; validation and train splits of v2) for a
research study in the course *Intelektualiosios sistemos* (VU MIF, 2026).
30 arguments where the conclusion follows and 30 where its negation follows;
all of them have 5 or more premises.

- `arguments.md` – the arguments: English text, FOLIO's FOL formulas, Seqprover sequents
- `sequents/` – Seqprover input files (`*.goal.pl` = conclusion, `*.neg.pl` = negated conclusion)
- `proofs/`, `results.md` – Seqprover output for every sequent
- `scripts/` – selection + FOL→Seqprover translation (`folio2seq.py`), prover runner (`run_seqprover.py`)
- `seqprover/` – [Seqprover](https://cspsat.gitlab.io/seqprover/) by N. Tamura, unmodified

Rebuild: `hf download yale-nlp/FOLIO --repo-type=dataset --local-dir data`,
then `python3 scripts/folio2seq.py build` and `python3 scripts/run_seqprover.py`
(needs SWI-Prolog).
