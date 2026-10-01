pretty.
(basedIn(system7,uk) /\ electronicDanceMusicBand(system7)), (form(stevehillage,system7) /\ form(miquettegiraudy,system7)), (formerMemberOf(stevehillage,gong) /\ formerMemberOf(miquettegiraudy,gong)), X@((electronicDanceMusicBand(X) -> band(X))), X#((clubSingle(X) /\ release(system7,X))), X@((clubSingle(X) -> ~single(X))) --> ~X#((form(X,system7) /\ formerMemberOf(X,gong))).
