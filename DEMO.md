# Running Seqprover by hand

Raw `swipl` commands for running single sequents without `scripts/run_seqprover.py`.
Run them from the repository root. Needs SWI-Prolog (`brew install swi-prolog`).

## Input format

Each file in `sequents/` is one Seqprover input: `pretty.` (print the proof as a tree),
then one sequent `premises --> conclusion.` Notation: `X@` = ∀X, `X#` = ∃X, `~` = ¬,
`/\` = ∧, `\/` = ∨, `->` = →. Example, `sequents/ARG-16.goal.pl`:

```
pretty.
X#((professional(X) /\ (basketballPlayer(X) /\ ~americanNational(X)))), X@(((professional(X) /\ basketballPlayer(X)) -> canDo(X,jumpShot))), X@((canDo(X,jumpShot) -> leapStraightIntoAir(X))), X@((leapStraightIntoAir(X) -> activate(X,legMuscle))), ~activate(yuri,legMuscle) --> ~(americanNational(yuri) /\ (professional(yuri) /\ basketballPlayer(yuri))).
```

`*.goal.pl` asks for the conclusion, `*.neg.pl` for its negation.

## 1. Proved (ARG-01, conclusion)

```
swipl -q -g "set_threshold(5),batch" seqprover/seqprover.pl < sequents/ARG-01.goal.pl
```

Prints the proof tree and ends with `# END Proof` and `# Proved in 4 msec.`

## 2. Not proved within the threshold (ARG-04, conclusion)

```
swipl -q -g "set_threshold(5),batch" seqprover/seqprover.pl < sequents/ARG-04.goal.pl
```

Ends with `Trying to prove with threshold = 0 1 2 3 4 5` and `# Fail to prove` (about 0.6 s).
The threshold caps the ∀-left / ∃-right / cut / contraction steps per proof path, so this
means "no proof up to 5", not "does not follow".

## 3. The slowest proof (ARG-16, conclusion)

```
swipl -q -g "set_threshold(5),batch" seqprover/seqprover.pl < sequents/ARG-16.goal.pl
```

Ends with `# Proved in 5585 msec.` (about 5.9 s wall time).

## 4. Search that does not stop (ARG-01, negated conclusion), with a time limit

```
swipl -q -g "catch(call_with_time_limit(10,(set_threshold(5),batch)),time_limit_exceeded,(writeln('# TIMEOUT'),halt))" seqprover/seqprover.pl < sequents/ARG-01.neg.pl
```

Prints `# TIMEOUT` after 10 s (about 0.7 GB memory at that point). Without the time limit
this keeps running and Seqprover's memoisation grows without bound, so always keep a limit
(and run at most two of these at once).

## Saving the output

Append `> out.txt` to any command. The files in `proofs/` were produced the same way by
`scripts/run_seqprover.py` (threshold 5, timeout 60 s).
