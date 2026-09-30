pretty.
X#((occurIn(monkeypoxVirus,X) /\ get(X,monkeypoxVirus))), X#((animal(X) /\ occurIn(monkeypoxVirus,X))), X@((human(X) -> mammal(X))), X@((mammal(X) -> animal(X))), X#((symptonOf(X,monkeypoxVirus) /\ (fever(X) \/ (headache(X) \/ (musclePain(X) \/ tired(X)))))), X@(((human(X) /\ get(X,flu)) -> feel(X,tired))) --> X#((symptonOf(X,monkeypoxVirus) /\ coughing(X))).
