pretty.
(team(goldenStateWarriors) /\ from(goldenStateWarriors,sanFrancisco)), won(goldenStateWarriors,nbaFinals), X@(((team(X) /\ attending(X,nbaFinals)) -> wonManyGames(X))), (team(bostonCeltics) /\ lost(bostonCeltics,nbaFinals)), X@(((team(X) /\ won(X,nbaFinals)) -> moreIncome(X))), X@(((won(X,nbaFinals) \/ lost(X,nbaFinals)) -> attending(X,nbaFinals))) --> ~moreIncome(goldenStateWarriors).
