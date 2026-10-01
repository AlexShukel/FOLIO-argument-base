pretty.
X@((businessOrganization(X) -> legalEntity(X))), X@((company(X) -> businessOrganization(X))), X@((privateCompany(X) -> company(X))), X@((legalEntity(X) -> createdUnderLaw(X))), X@((legalEntity(X) -> legalObligation(X))), (createdUnderLaw(harvardWeeklyBookClub) -> ~privateCompany(harvardWeeklyBookClub)) --> (legalObligation(harvardWeeklyBookClub) /\ privateCompany(harvardWeeklyBookClub)).
