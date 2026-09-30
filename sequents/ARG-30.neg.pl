pretty.
X@((romanceLanguage(X) -> indoEuropeanLanguage(X))), X@((romanceLanguage(X) -> memberOf(X,languageFamily))), X@(Y@(Z@(((memberOf(X,Z) /\ memberOf(Y,Z)) -> (related(X,Y) /\ related(Y,X)))))), (romanceLanguage(french) /\ romanceLanguage(spanish)), related(german,spanish), X@((language(X) -> ~related(basque,X))) --> ~romanceLanguage(basque).
