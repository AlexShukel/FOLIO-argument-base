# Curated FOLIO argument base (60 arguments)

Source: folio_v2_validation.jsonl + folio_v2_train.jsonl. Labels: True = conclusion follows; False = negation of the conclusion follows.

| ID | FOLIO split | FOLIO id | Story | Label | Premises |
|---|---|---|---|---|---|
| ARG-01 | validation | 0 | 0 | True | 6 |
| ARG-02 | validation | 243 | 80 | True | 5 |
| ARG-03 | validation | 253 | 83 | True | 5 |
| ARG-04 | validation | 388 | 131 | True | 5 |
| ARG-05 | validation | 440 | 151 | True | 5 |
| ARG-06 | validation | 560 | 197 | True | 6 |
| ARG-07 | validation | 563 | 198 | True | 6 |
| ARG-08 | validation | 578 | 203 | True | 5 |
| ARG-09 | validation | 610 | 213 | True | 6 |
| ARG-10 | validation | 657 | 232 | True | 6 |
| ARG-11 | validation | 806 | 319 | True | 5 |
| ARG-12 | validation | 808 | 319 | True | 5 |
| ARG-13 | validation | 1033 | 386 | True | 6 |
| ARG-14 | validation | 1269 | 441 | True | 5 |
| ARG-15 | validation | 1273 | 442 | True | 5 |
| ARG-16 | validation | 1314 | 456 | True | 5 |
| ARG-17 | validation | 1412 | 483 | True | 6 |
| ARG-18 | train | 17 | 7 | True | 9 |
| ARG-19 | train | 18 | 7 | True | 9 |
| ARG-20 | train | 35 | 13 | True | 6 |
| ARG-21 | train | 38 | 14 | True | 5 |
| ARG-22 | train | 39 | 14 | True | 5 |
| ARG-23 | train | 61 | 21 | True | 6 |
| ARG-24 | train | 62 | 21 | True | 6 |
| ARG-25 | train | 65 | 22 | True | 6 |
| ARG-26 | train | 67 | 23 | True | 5 |
| ARG-27 | train | 101 | 35 | True | 5 |
| ARG-28 | train | 110 | 38 | True | 5 |
| ARG-29 | train | 111 | 38 | True | 5 |
| ARG-30 | train | 119 | 41 | True | 5 |
| ARG-31 | validation | 1 | 0 | False | 6 |
| ARG-32 | validation | 254 | 83 | False | 5 |
| ARG-33 | validation | 304 | 101 | False | 5 |
| ARG-34 | validation | 305 | 101 | False | 5 |
| ARG-35 | validation | 306 | 101 | False | 5 |
| ARG-36 | validation | 389 | 131 | False | 5 |
| ARG-37 | validation | 441 | 151 | False | 5 |
| ARG-38 | validation | 562 | 197 | False | 6 |
| ARG-39 | validation | 580 | 203 | False | 5 |
| ARG-40 | validation | 608 | 213 | False | 6 |
| ARG-41 | validation | 805 | 319 | False | 5 |
| ARG-42 | validation | 934 | 352 | False | 6 |
| ARG-43 | validation | 1034 | 386 | False | 6 |
| ARG-44 | validation | 1272 | 442 | False | 5 |
| ARG-45 | validation | 1315 | 456 | False | 5 |
| ARG-46 | validation | 1316 | 456 | False | 5 |
| ARG-47 | train | 19 | 7 | False | 9 |
| ARG-48 | train | 37 | 13 | False | 6 |
| ARG-49 | train | 40 | 14 | False | 5 |
| ARG-50 | train | 63 | 22 | False | 6 |
| ARG-51 | train | 102 | 35 | False | 5 |
| ARG-52 | train | 178 | 60 | False | 7 |
| ARG-53 | train | 179 | 60 | False | 7 |
| ARG-54 | train | 193 | 65 | False | 7 |
| ARG-55 | train | 196 | 66 | False | 10 |
| ARG-56 | train | 199 | 67 | False | 7 |
| ARG-57 | train | 202 | 68 | False | 8 |
| ARG-58 | train | 205 | 69 | False | 5 |
| ARG-59 | train | 239 | 78 | False | 5 |
| ARG-60 | train | 318 | 105 | False | 5 |

## ARG-01 — True (FOLIO validation example 0, story 0)

**Premises**

- There are six types of wild turkeys: Eastern wild turkey, Osceola wild turkey, Gould’s wild turkey, Merriam’s wild turkey, Rio Grande wild turkey, and Ocellated wild turkey.  
  `∀x (WildTurkey(x) → (EasternWildTurkey(x) ∨ OsceolaWildTurkey(x) ∨ GouldsWildTurkey(x) ∨ MerriamsWildTurkey(x) ∨ RiograndeWildTurkey(x) ∨ OcellatedWildTurkey(x)))`
- Tom is not an Eastern wild turkey.  
  `¬(EasternWildTurkey(tom))`
- Tom is not an Osceola wild turkey.  
  `¬(OsceolaWildTurkey(tom))`
- Tom is not a Gould's wild turkey.  
  `¬(GouldsWildTurkey(tom))`
- Tom is neither a Merriam's wild turkey nor a Rio Grande wild turkey.  
  `¬(MerriamsWildTurkey(tom) ∨ RiograndeWildTurkey(tom))`
- Tom is a wild turkey.  
  `WildTurkey(tom)`

**Conclusion**

- Tom is an Ocellated wild turkey.  
  `OcellatedWildTurkey(tom)`

**Seqprover**

```
X@((wildTurkey(X) -> (easternWildTurkey(X) \/ (osceolaWildTurkey(X) \/ (gouldsWildTurkey(X) \/ (merriamsWildTurkey(X) \/ (riograndeWildTurkey(X) \/ ocellatedWildTurkey(X)))))))), ~easternWildTurkey(tom), ~osceolaWildTurkey(tom), ~gouldsWildTurkey(tom), ~(merriamsWildTurkey(tom) \/ riograndeWildTurkey(tom)), wildTurkey(tom) --> ocellatedWildTurkey(tom)
```

## ARG-02 — True (FOLIO validation example 243, story 80)

**Premises**

- New Vessel Press is a publishing house specializing in translating foreign literature into English.  
  `PublishingHouse(newVesselPress) ∧ SpecializesInTranslatingIntoEnglish(newVesselPress, foreignLiterature)`
- All of New Vessel Press's published books are in English.  
  `∀x ((Book(x) ∧ PublishedBy(x, newVesselPress)) → In(x, english))`
- Neapolitan Chronicles is a book published by New Vessel Press.  
  `Book(neapolitanChronicles) ∧ PublishedBy(neapolitanChronicles, newVesselPress)`
- Neapolitan Chronicles was translated from Italian.  
  `TranslatedFrom(neapolitanChronicles, italian)`
- Palace of Flies is a book published by New Vessel Press.  
  `Book(palaceOfFlies) ∧ PublishedBy(palaceOfFlies, newVesselPress)`

**Conclusion**

- Neapolitan Chronicles is an English book.  
  `Book(neapolitanChronicles) ∧ In(neapolitanChronicles, english)`

**Seqprover**

```
(publishingHouse(newVesselPress) /\ specializesInTranslatingIntoEnglish(newVesselPress,foreignLiterature)), X@(((book(X) /\ publishedBy(X,newVesselPress)) -> in(X,english))), (book(neapolitanChronicles) /\ publishedBy(neapolitanChronicles,newVesselPress)), translatedFrom(neapolitanChronicles,italian), (book(palaceOfFlies) /\ publishedBy(palaceOfFlies,newVesselPress)) --> (book(neapolitanChronicles) /\ in(neapolitanChronicles,english))
```

## ARG-03 — True (FOLIO validation example 253, story 83)

**Premises**

- All vehicle registration plates in Istanbul begin with the number 34.  
  `∀x (VehicleRegistrationPlateIn(x, istanbul) → BeginWith(x, num34))`
- Plates that do not begin with the number 34 are not from Istanbul.  
  `∀x (¬BeginWith(x, num34) → ¬FromIstanbul(x))`
- Joe's vehicle registration plate is from Istanbul.  
  `∃x (Owns(joe, x) ∧ VehicleRegistrationPlateIn(x, istanbul))`
- Tom's license plate begins with the number 35.  
  `∃x (Owns(tom, x) ∧ BeginWith(x, num35))`
- If a license plate begins with the number 35, then it does not begin with the number 34.  
  `∀x (BeginWith(x, num35) → ¬BeginWith(x, num34))`

**Conclusion**

- Joe's license plate begins with the number 34.  
  `∃x (Owns(joe, x) ∧ BeginWith(x, num34))`

**Seqprover**

```
X@((vehicleRegistrationPlateIn(X,istanbul) -> beginWith(X,num34))), X@((~beginWith(X,num34) -> ~fromIstanbul(X))), X#((owns(joe,X) /\ vehicleRegistrationPlateIn(X,istanbul))), X#((owns(tom,X) /\ beginWith(X,num35))), X@((beginWith(X,num35) -> ~beginWith(X,num34))) --> X#((owns(joe,X) /\ beginWith(X,num34)))
```

## ARG-04 — True (FOLIO validation example 388, story 131)

**Premises**

- Machine Learning algorithms can be categorized as supervised learning, unsupervised learning, and reinforcement learning.  
  `∀x (MachineLearningAlgorithm(x) → SupervisedLearningAlgorithm(x) ∨ UnsupervisedLearningAlgorithm(x) ∨ ReinforcementLearningAlgorithm(x))`
- Unsupervised learning algorithms do not require labeled data.  
  `∀x (UnsupervisedLearningAlgorithm(x) → ¬Require(x, labeledData))`
- The state-of-the-art text summarization model is trained with machine learning algorithms.  
  `∀x (TrainedWith(stateOfTheArtTextSummarizationModel, x) → MachineLearningAlgorithm(x))`
- Reinforcement learning is not used to train the state-of-the-art text summarization model.  
  `∀x (ReinforcementLearningAlgorithm(x) → ¬TrainedWith(stateOfTheArtTextSummarizationModel, x))`
- The Machine Learning algorithm for training text summarization models requires labeled data.  
  `∀x ((MachineLearningAlgorithm(x) ∧ TrainedWith(stateOfTheArtTextSummarizationModel, x)) → Require(x, labeledData))`

**Conclusion**

- Supervised learning is used to train the state-of-the-art text summarization model.  
  `∃x (SupervisedLearningAlgorithm(x) ∧ TrainedWith(stateOfTheArtTextSummarizationModel, x))`

**Seqprover**

```
X@((machineLearningAlgorithm(X) -> (supervisedLearningAlgorithm(X) \/ (unsupervisedLearningAlgorithm(X) \/ reinforcementLearningAlgorithm(X))))), X@((unsupervisedLearningAlgorithm(X) -> ~require(X,labeledData))), X@((trainedWith(stateOfTheArtTextSummarizationModel,X) -> machineLearningAlgorithm(X))), X@((reinforcementLearningAlgorithm(X) -> ~trainedWith(stateOfTheArtTextSummarizationModel,X))), X@(((machineLearningAlgorithm(X) /\ trainedWith(stateOfTheArtTextSummarizationModel,X)) -> require(X,labeledData))) --> X#((supervisedLearningAlgorithm(X) /\ trainedWith(stateOfTheArtTextSummarizationModel,X)))
```

## ARG-05 — True (FOLIO validation example 440, story 151)

**Premises**

- Barutin Cove is a cove named after the Bulgarian settlement of Barutin.  
  `Cove(barutinCove) ∧ NamedAfter(barutinCove, barutinSettlement) ∧ LocatedIn(barutinSettlement, bulgaria)`
- Barutin Cove is on the southwest coast of Snow Island.  
  `LocatedIn(barutinCove, snowIsland)`
- Snow Island, Greenwich Island, and Deception Island are located in the South Shetland Islands.  
  `LocatedIn(snowIsland, southShetlandIslands) ∧ LocatedIn(greenwichIsland, southShetlandIslands) ∧ LocatedIn(deceptionIsland, southShetlandIslands)`
- Antarctica is located on the South Shetland Islands.  
  `LocatedIn(southShetlandIslands, antarctica)`
- If place A is located in place B and place B is located in place C, then place A is located in place C.  
  `∀x ∀y ∀z ((LocatedIn(x, y) ∧ LocatedIn(y, z)) → LocatedIn(x, z))`

**Conclusion**

- There is at least one cove in Antarctica named after a place in Bulgaria.  
  `∃x ∃y (Cove(x) ∧ LocatedIn(x, antarctica) ∧ NameAfter(x, y) ∧ LocatedIn(y, bulgaria))`

**Seqprover**

```
(cove(barutinCove) /\ (namedAfter(barutinCove,barutinSettlement) /\ locatedIn(barutinSettlement,bulgaria))), locatedIn(barutinCove,snowIsland), (locatedIn(snowIsland,southShetlandIslands) /\ (locatedIn(greenwichIsland,southShetlandIslands) /\ locatedIn(deceptionIsland,southShetlandIslands))), locatedIn(southShetlandIslands,antarctica), X@(Y@(Z@(((locatedIn(X,Y) /\ locatedIn(Y,Z)) -> locatedIn(X,Z))))) --> X#(Y#((cove(X) /\ (locatedIn(X,antarctica) /\ (nameAfter(X,Y) /\ locatedIn(Y,bulgaria))))))
```

## ARG-06 — True (FOLIO validation example 560, story 197)

**Premises**

- It costs $205 to take the GRE test, which is cheaper than $300.  
  `Cost(gRE, 205) ∧ Cheaper(205, 300)`
- ETS provides financial aid to those GRE applicants who prove economic hardship.  
  `∀x (ApplicantOf(x, gre) ∧ Prove(x, economicHardship) → ProvideTo(ets, financialAid, x))`
- Those living in single-parent families or having few resources available to them can prove economic hardship.  
  `∀x (LivingIn(x, singleParentFamily) ∨ AvailableTo(fewResources, x) → Prove(x, economicHardship))`
- Tom lives in a single-parent family.  
  `LivingIn(tom, singleParentFamily)`
- Tom's dad has been out of work, and Tom has few resources available to them.  
  `OutOfWork(tomsDad) ∧ AvailableTo(fewResources, tom)`
- Tom is applying to take the GRE test.  
  `ApplicantOf(tom, gre)`

**Conclusion**

- ETS provides financial aid to Tom.  
  `ProvidesFinancialAidTo(eTS, tom)`

**Seqprover**

```
(cost(gRE,205) /\ cheaper(205,300)), X@(((applicantOf(X,gre) /\ prove(X,economicHardship)) -> provideTo(ets,financialAid,X))), X@(((livingIn(X,singleParentFamily) \/ availableTo(fewResources,X)) -> prove(X,economicHardship))), livingIn(tom,singleParentFamily), (outOfWork(tomsDad) /\ availableTo(fewResources,tom)), applicantOf(tom,gre) --> providesFinancialAidTo(eTS,tom)
```

## ARG-07 — True (FOLIO validation example 563, story 198)

**Premises**

- When the Monkeypox virus occurs in a being, it may get Monkeypox.  
  `∃x (OccurIn(monkeypoxVirus, x) ∧ Get(x, monkeypoxVirus))`
- Monkeypox virus can occur in certain animals.  
  `∃x (Animal(x) ∧ OccurIn(monkeypoxVirus, x))`
- Humans are mammals.  
  `∀x (Human(x) → Mammal(x))`
- Mammals are animals.  
  `∀x (Mammal(x) → Animal(x))`
- Symptoms of Monkeypox include fever, headache, muscle pains, and tiredness.  
  `∃x (SymptonOf(x, monkeypoxVirus) ∧ (Fever(x) ∨ Headache(x) ∨ MusclePain(x) ∨ Tired(x)))`
- People feel tired when they get the flu.  
  `∀x (Human(x) ∧ Get(x, flu) → Feel(x, tired))`

**Conclusion**

- There is an animal.  
  `∃x (Animal(x))`

**Seqprover**

```
X#((occurIn(monkeypoxVirus,X) /\ get(X,monkeypoxVirus))), X#((animal(X) /\ occurIn(monkeypoxVirus,X))), X@((human(X) -> mammal(X))), X@((mammal(X) -> animal(X))), X#((symptonOf(X,monkeypoxVirus) /\ (fever(X) \/ (headache(X) \/ (musclePain(X) \/ tired(X)))))), X@(((human(X) /\ get(X,flu)) -> feel(X,tired))) --> X#(animal(X))
```

## ARG-08 — True (FOLIO validation example 578, story 203)

**Premises**

- Plungers suck.  
  `∀x (Plunger(x) → Suck(x))`
- Vacuums suck.  
  `∀x (Vacuum(x) → Suck(x))`
- Vampires suck.  
  `∀x (Vampire(x) → Suck(x))`
- Space is a vacuum.  
  `Vacuum(space)`
- A duster is a household appliance that doesn't suck.  
  `HouseholdAppliance(duster) ∧ ¬Suck(duster)`

**Conclusion**

- Space sucks.  
  `Suck(space)`

**Seqprover**

```
X@((plunger(X) -> suck(X))), X@((vacuum(X) -> suck(X))), X@((vampire(X) -> suck(X))), vacuum(space), (householdAppliance(duster) /\ ~suck(duster)) --> suck(space)
```

## ARG-09 — True (FOLIO validation example 610, story 213)

**Premises**

- All Romance languages are Indo-European languages.  
  `∀x (RomanceLanguage(x) → IndoEuropeanLanguage(x))`
- Romance languages are a language family.  
  `∀x (RomanceLanguage(x) → MemberOf(x, languageFamily))`
- All languages within a language family are related to each other.  
  `∀x ∀y ∀z ((MemberOf(x, z) ∧ MemberOf(y, z)) → (Related(x, y) ∧ Related(y, x)))`
- French and Spanish are both Romance languages.  
  `RomanceLanguage(french) ∧ RomanceLanguage(spanish)`
- German is related to Spanish.  
  `Related(german, spanish)`
- Basque is not related to any other language.  
  `∀x (Language(x) → ¬Related(basque, x))`

**Conclusion**

- French is an Indo-European language.  
  `IndoEuropeanLanguage(french)`

**Seqprover**

```
X@((romanceLanguage(X) -> indoEuropeanLanguage(X))), X@((romanceLanguage(X) -> memberOf(X,languageFamily))), X@(Y@(Z@(((memberOf(X,Z) /\ memberOf(Y,Z)) -> (related(X,Y) /\ related(Y,X)))))), (romanceLanguage(french) /\ romanceLanguage(spanish)), related(german,spanish), X@((language(X) -> ~related(basque,X))) --> indoEuropeanLanguage(french)
```

## ARG-10 — True (FOLIO validation example 657, story 232)

**Premises**

- Beijing is the capital of the People's Republic of China.  
  `CapitalOf(beijing, peoplesRepublicOfChina)`
- Beijing is the capital city of the world's most populous nation.  
  `∃x (CapitalOf(beijing, x) → WorldsMostPopulousNation(x))`
- Beijing is located in Northern China.  
  `LocatedIn(beijing, northernChina)`
- Beijing hosted the 2008 Summer Olympics and 2008 Summer Paralympics Games.  
  `Hosted(beijing, 2008SummerOlympics) ∧ Hosted(beijing, 2008SummerParalympicGames)`
- Beijing has hosted the Summer and Winter Olympics and the Summer and Winter Paralympics.  
  `Hosted(beijing, summerOlympics) ∧ Hosted(beijing, winterOlympics) ∧ Hosted(beijing, summerParalympicGames)  ∧ Hosted(beijing, winterParalympicGames)`
- Many of Beijing's 91 universities consistently rank among the best universities in the world.  
  `∃x (University(x) ∧ InBeijing(x) ∧ ConsistentlyRankAmongTheBestIn(x, theWorld))`

**Conclusion**

- Beijing hosted both the 2008 Summer Olympics and the Winter Olympics.  
  `Hosted(beijing, summerOlympics) ∧ Hosted(beijing, winterOlympics)`

**Seqprover**

```
capitalOf(beijing,peoplesRepublicOfChina), X#((capitalOf(beijing,X) -> worldsMostPopulousNation(X))), locatedIn(beijing,northernChina), (hosted(beijing,'2008SummerOlympics') /\ hosted(beijing,'2008SummerParalympicGames')), (hosted(beijing,summerOlympics) /\ (hosted(beijing,winterOlympics) /\ (hosted(beijing,summerParalympicGames) /\ hosted(beijing,winterParalympicGames)))), X#((university(X) /\ (inBeijing(X) /\ consistentlyRankAmongTheBestIn(X,theWorld)))) --> (hosted(beijing,summerOlympics) /\ hosted(beijing,winterOlympics))
```

## ARG-11 — True (FOLIO validation example 806, story 319)

**Premises**

- No baked sweets are spicy.  
  `∀x (BakedSweet(x) → ¬Spicy(x))`
- All cupcakes are baked sweets.  
  `∀x (Cupcake(x) → BakedSweet(x))`
- All mala hotpots are spicy.  
  `∀x (MalaHotpot(x) → Spicy(x))`
- All products from Baked by Melissa are cupcakes.  
  `∀x (Product(x) ∧ From(x, bakedByMelissa) → Cupcake(x))`
- Dried Thai chilies are spicy or mala hotpots or not baked sweets.  
  `Spicy(driedThaiChili) ∨ MalaHotpot(driedThaiChili)∨ ¬BakedSweet(driedThaiChili)`

**Conclusion**

- Dried Thai chilies are not products of Baked by Melissa.  
  `¬(Product(driedThaiChili) ∧ From(driedThaiChili, bakedByMelissa))`

**Seqprover**

```
X@((bakedSweet(X) -> ~spicy(X))), X@((cupcake(X) -> bakedSweet(X))), X@((malaHotpot(X) -> spicy(X))), X@(((product(X) /\ from(X,bakedByMelissa)) -> cupcake(X))), (spicy(driedThaiChili) \/ (malaHotpot(driedThaiChili) \/ ~bakedSweet(driedThaiChili))) --> ~(product(driedThaiChili) /\ from(driedThaiChili,bakedByMelissa))
```

## ARG-12 — True (FOLIO validation example 808, story 319)

**Premises**

- No baked sweets are spicy.  
  `∀x (BakedSweet(x) → ¬Spicy(x))`
- All cupcakes are baked sweets.  
  `∀x (Cupcake(x) → BakedSweet(x))`
- All mala hotpots are spicy.  
  `∀x (MalaHotpot(x) → Spicy(x))`
- All products from Baked by Melissa are cupcakes.  
  `∀x (Product(x) ∧ From(x, bakedByMelissa) → Cupcake(x))`
- Dried Thai chilies are spicy or mala hotpots or not baked sweets.  
  `Spicy(driedThaiChili) ∨ MalaHotpot(driedThaiChili)∨ ¬BakedSweet(driedThaiChili)`

**Conclusion**

- Dried Thai chilies are neither products of Baked by Melissa nor baked sweets.  
  `¬(Product(driedThaiChili) ∧ From(driedThaiChili, bakedByMelissa)) ∧ ¬BakedSweet(driedThaiChili)`

**Seqprover**

```
X@((bakedSweet(X) -> ~spicy(X))), X@((cupcake(X) -> bakedSweet(X))), X@((malaHotpot(X) -> spicy(X))), X@(((product(X) /\ from(X,bakedByMelissa)) -> cupcake(X))), (spicy(driedThaiChili) \/ (malaHotpot(driedThaiChili) \/ ~bakedSweet(driedThaiChili))) --> (~(product(driedThaiChili) /\ from(driedThaiChili,bakedByMelissa)) /\ ~bakedSweet(driedThaiChili))
```

## ARG-13 — True (FOLIO validation example 1033, story 386)

**Premises**

- If something is a deadly disease, then it comes with a low survival rate.  
  `∀x (DeadlyDiseases(x) → ComeWith(x, lowSurvivalRate))`
- Severe cancers are deadly diseases.  
  `∀x (SevereCancer(x) → DeadlyDiseases(x))`
- Bile duct cancer is a severe form cancer.  
  `∀x (BileDuctCancer(x) → SevereCancer(x))`
- All Cholangiocarcinoma is bile duct cancer.  
  `∀x (Cholangiocarcinoma(x) → BileDuctCancer(x))`
- Mild flu comes with a low survival rate.  
  `∀x (MildFlu(x) → ¬ComeWith(x, lowSurvivalRate))`
- Colorectal cancer is not both a bile duct cancer and with a low survival rate.  
  `¬(BileDuctCancer(colorectalCancer) ∧ ComeWith(colorectalCancer, lowSurvivalRate))`

**Conclusion**

- If colorectal cancer is a kind of bile duct cancer or a form of Cholangiocarcinoma, then colorectal cancer is a kind of bile duct cancer and a kind of mild flu.  
  `¬(BileDuctCancer(colorectalCancer) ∨ Cholangiocarcinoma(colorectalCancer)) ∨ (BileDuctCancer(colorectalCancer) ∧ MildFlu(colorectalCancer))`

**Seqprover**

```
X@((deadlyDiseases(X) -> comeWith(X,lowSurvivalRate))), X@((severeCancer(X) -> deadlyDiseases(X))), X@((bileDuctCancer(X) -> severeCancer(X))), X@((cholangiocarcinoma(X) -> bileDuctCancer(X))), X@((mildFlu(X) -> ~comeWith(X,lowSurvivalRate))), ~(bileDuctCancer(colorectalCancer) /\ comeWith(colorectalCancer,lowSurvivalRate)) --> (~(bileDuctCancer(colorectalCancer) \/ cholangiocarcinoma(colorectalCancer)) \/ (bileDuctCancer(colorectalCancer) /\ mildFlu(colorectalCancer)))
```

## ARG-14 — True (FOLIO validation example 1269, story 441)

**Premises**

- No one nice to animals is also mean to animals.  
  `∀x (NiceTo(x, animal) → ¬MeanTo(x, animal))`
- Some grumpy people are mean to animals.  
  `∃x (Grumpy(x) ∧ MeanTo(x, animal))`
- All animal lovers are nice to animals.  
  `∀x (AnimalLover(x) → NiceTo(x, animal))`
- All pet owners love animals.  
  `∀x (PetOwner(x) → AnimalLover(x))`
- Tom is a pet owner.  
  `PetOwner(tom)`

**Conclusion**

- Tom is not both a grumpy person and mean to animals.  
  `¬(Grumpy(tom) ∧ MeanTo(tom, animal))`

**Seqprover**

```
X@((niceTo(X,animal) -> ~meanTo(X,animal))), X#((grumpy(X) /\ meanTo(X,animal))), X@((animalLover(X) -> niceTo(X,animal))), X@((petOwner(X) -> animalLover(X))), petOwner(tom) --> ~(grumpy(tom) /\ meanTo(tom,animal))
```

## ARG-15 — True (FOLIO validation example 1273, story 442)

**Premises**

- All Brown Swiss cattle are cows.  
  `∀x (BrownSwissCattle(x) → Cow(x))`
- Some pets are Brown Swiss Cattle.  
  `∃x (Pet(x) ∧ BrownSwissCattle(x))`
- All cows are domesticated animals.  
  `∀x (Cow(x) → DomesticatedAnimal(x))`
- Alligators are not domesticated animals.  
  `∀x (Aligator(x) → ¬DomesticatedAnimal(x))`
- Ted is an alligator.  
  `Aligator(ted)`

**Conclusion**

- If Ted is a Brown Swiss cattle, then Ted is not a pet.  
  `BrownSwissCattle(ted) → ¬Pet(ted)`

**Seqprover**

```
X@((brownSwissCattle(X) -> cow(X))), X#((pet(X) /\ brownSwissCattle(X))), X@((cow(X) -> domesticatedAnimal(X))), X@((aligator(X) -> ~domesticatedAnimal(X))), aligator(ted) --> (brownSwissCattle(ted) -> ~pet(ted))
```

## ARG-16 — True (FOLIO validation example 1314, story 456)

**Premises**

- Some professional basketball players are not American nationals.  
  `∃x (Professional(x) ∧ BasketballPlayer(x) ∧ ¬AmericanNational(x))`
- All professional basketball players can do jump shots.  
  `∀x (Professional(x) ∧ BasketballPlayer(x) → CanDo(x, jumpShot))`
- If someone can jump shots, they leap straight into the air.  
  `∀x (CanDo(x, jumpShot) → LeapStraightIntoAir(x))`
- If someone leaps straight into the air, they activate their leg muscles.  
  `∀x (LeapStraightIntoAir(x) → Activate(x, legMuscle))`
- Yuri does not activate his leg muscles.  
  `¬Activate(yuri, legMuscle)`

**Conclusion**

- Yuri is not an American professional basketball player.  
  `¬(AmericanNational(yuri) ∧ Professional(yuri) ∧ BasketballPlayer(yuri))`

**Seqprover**

```
X#((professional(X) /\ (basketballPlayer(X) /\ ~americanNational(X)))), X@(((professional(X) /\ basketballPlayer(X)) -> canDo(X,jumpShot))), X@((canDo(X,jumpShot) -> leapStraightIntoAir(X))), X@((leapStraightIntoAir(X) -> activate(X,legMuscle))), ~activate(yuri,legMuscle) --> ~(americanNational(yuri) /\ (professional(yuri) /\ basketballPlayer(yuri)))
```

## ARG-17 — True (FOLIO validation example 1412, story 483)

**Premises**

- Everyone who can register to vote in the United States can participate in the 2024 United States presidential election.  
  `∀x (CanRegisterToVoteIn(x, unitedStates) → CanParticipateIn(x, 2024UnitedStatesElection))`
- If someone has United States citizenship, then they can register to vote in the United States.  
  `∀x (Have(x, unitedStatesCitizenship) → CanRegisterToVoteIn(x, unitedStates))`
- A person either has United States citizenship or Taiwanese citizenship.  
  `∀x (Have(x, unitedStatesCitizenship) ∨ Have(x, taiwaneseCitizenship))`
- No Russian Federation officials hold Taiwanese citizenship.  
  `∀x (Russian(x) ∧ FederationOfficial(x) → ¬Have(x, taiwaneseCitizenship))`
- Vladimir neither holds Taiwanese citizenship nor is he a manager at Gazprom.  
  `¬Have(vladimir, taiwaneseCitizenship) ∧ ¬ManagerAt(vladimir, gazprom)`
- Ekaterina she can register to vote in the United States, or she is a Russian federation official.  
  `(Russian(ekaterina) ∧ FederationOfficial(ekaterina)) ∨ CanRegisterToVoteIn(ekaterina, unitedStates)`

**Conclusion**

- Ekaterina can participate in the 2024 United States presidential election or is a manager at Gazprom.  
  `CanParticipateIn(ekaterina, 2024UnitedStatesElection) ∨ ManagerAt(ekaterina, gazprom)`

**Seqprover**

```
X@((canRegisterToVoteIn(X,unitedStates) -> canParticipateIn(X,'2024UnitedStatesElection'))), X@((have(X,unitedStatesCitizenship) -> canRegisterToVoteIn(X,unitedStates))), X@((have(X,unitedStatesCitizenship) \/ have(X,taiwaneseCitizenship))), X@(((russian(X) /\ federationOfficial(X)) -> ~have(X,taiwaneseCitizenship))), (~have(vladimir,taiwaneseCitizenship) /\ ~managerAt(vladimir,gazprom)), ((russian(ekaterina) /\ federationOfficial(ekaterina)) \/ canRegisterToVoteIn(ekaterina,unitedStates)) --> (canParticipateIn(ekaterina,'2024UnitedStatesElection') \/ managerAt(ekaterina,gazprom))
```

## ARG-18 — True (FOLIO train example 17, story 7)

**Premises**

- Six, seven and eight are real numbers.  
  `RealNum(num6) ∧ RealNum(num7) ∧ RealNum(num8)`
- If a real number equals another real number added by one, the first number is larger.  
  `∀x ∀y ((RealNum(x) ∧ RealNum(y) ∧ IsSuccessorOf(x, y)) → Larger(x, y))`
- If the number x is larger than the number y, then y is not larger than x.  
  `∀x ∀y (Larger(x, y) → ¬Larger(y, x))`
- Seven equals six plus one.  
  `∃y(IsSuccessorOf(y, num6) ∧ Equals(num7, y))`
- Eight equals seven plus one.  
  `∃y(IsSuccessorOf(y, num7) ∧ Equals(num8, y))`
- Two is positive.  
  `Positive(num2)`
- If a number is positive, then the double of it is also positive.  
  `∀x ∀y ((Positive(x) ∧ IsDouble(y, x)) → Positive(y))`
- Eight is the double of four.  
  `IsDouble(num8, num4)`
- Four is the double of two.  
  `IsDouble(num4, num2)`

**Conclusion**

- Eight is larger than seven.  
  `Larger(eight, seven)`

**Seqprover**

```
(realNum(num6) /\ (realNum(num7) /\ realNum(num8))), X@(Y@(((realNum(X) /\ (realNum(Y) /\ isSuccessorOf(X,Y))) -> larger(X,Y)))), X@(Y@((larger(X,Y) -> ~larger(Y,X)))), Y#((isSuccessorOf(Y,num6) /\ equals(num7,Y))), Y#((isSuccessorOf(Y,num7) /\ equals(num8,Y))), positive(num2), X@(Y@(((positive(X) /\ isDouble(Y,X)) -> positive(Y)))), isDouble(num8,num4), isDouble(num4,num2) --> larger(eight,seven)
```

## ARG-19 — True (FOLIO train example 18, story 7)

**Premises**

- Six, seven and eight are real numbers.  
  `RealNum(num6) ∧ RealNum(num7) ∧ RealNum(num8)`
- If a real number equals another real number added by one, the first number is larger.  
  `∀x ∀y ((RealNum(x) ∧ RealNum(y) ∧ IsSuccessorOf(x, y)) → Larger(x, y))`
- If the number x is larger than the number y, then y is not larger than x.  
  `∀x ∀y (Larger(x, y) → ¬Larger(y, x))`
- Seven equals six plus one.  
  `∃y(IsSuccessorOf(y, num6) ∧ Equals(num7, y))`
- Eight equals seven plus one.  
  `∃y(IsSuccessorOf(y, num7) ∧ Equals(num8, y))`
- Two is positive.  
  `Positive(num2)`
- If a number is positive, then the double of it is also positive.  
  `∀x ∀y ((Positive(x) ∧ IsDouble(y, x)) → Positive(y))`
- Eight is the double of four.  
  `IsDouble(num8, num4)`
- Four is the double of two.  
  `IsDouble(num4, num2)`

**Conclusion**

- Eight is positive.  
  `Positive(eight)`

**Seqprover**

```
(realNum(num6) /\ (realNum(num7) /\ realNum(num8))), X@(Y@(((realNum(X) /\ (realNum(Y) /\ isSuccessorOf(X,Y))) -> larger(X,Y)))), X@(Y@((larger(X,Y) -> ~larger(Y,X)))), Y#((isSuccessorOf(Y,num6) /\ equals(num7,Y))), Y#((isSuccessorOf(Y,num7) /\ equals(num8,Y))), positive(num2), X@(Y@(((positive(X) /\ isDouble(Y,X)) -> positive(Y)))), isDouble(num8,num4), isDouble(num4,num2) --> positive(eight)
```

## ARG-20 — True (FOLIO train example 35, story 13)

**Premises**

- System 7 is a UK-based electronic dance music band.  
  `BasedIn(system7, uk) ∧ ElectronicDanceMusicBand(system7)`
- Steve Hillage and Miquette Giraudy formed System 7.  
  `Form(stevehillage, system7) ∧ Form(miquettegiraudy, system7)`
- Steve Hillage and Miquette Giraudy are former members of the band Gong.  
  `FormerMemberOf(stevehillage, gong) ∧ FormerMemberOf(miquettegiraudy, gong)`
- Electric dance music bands are bands.  
  `∀x (ElectronicDanceMusicBand(x) → Band(x))`
- System 7 has released several club singles.  
  `∃x (ClubSingle(x) ∧ Release(system7, x))`
- Club singles are not singles.  
  `∀x (ClubSingle(x) → ¬Single(x))`

**Conclusion**

- System 7 was formed by former members of Gong.  
  `∃x (Form(x, system7) ∧ FormerMemberOf(x, gong))`

**Seqprover**

```
(basedIn(system7,uk) /\ electronicDanceMusicBand(system7)), (form(stevehillage,system7) /\ form(miquettegiraudy,system7)), (formerMemberOf(stevehillage,gong) /\ formerMemberOf(miquettegiraudy,gong)), X@((electronicDanceMusicBand(X) -> band(X))), X#((clubSingle(X) /\ release(system7,X))), X@((clubSingle(X) -> ~single(X))) --> X#((form(X,system7) /\ formerMemberOf(X,gong)))
```

## ARG-21 — True (FOLIO train example 38, story 14)

**Premises**

- The USS Salem is a heavy cruiser built for the United States Navy.  
  `HeavyCruiser(usssalem) ∧ BuiltFor(usssalem, unitedstatesnavy)`
- The last heavy cruiser to enter service was the USS Salem.  
  `LastHeavyCruiserToEnterService(usssalem)`
- The USS Salem is a museum ship.  
  `MuseumShip(usssalem)`
- Museum ships are open to the public.  
  `∀x (MuseumShip(x) → OpenToPublic(x))`
- The USS Salem served in the Atlantic and Mediterranean.  
  `ServedIn(usssalem, atlantic) ∧ ServedIn(usssalem, mediterranean)`

**Conclusion**

- The USS Salem is open to the public.  
  `OpenToPublic(usssalem)`

**Seqprover**

```
(heavyCruiser(usssalem) /\ builtFor(usssalem,unitedstatesnavy)), lastHeavyCruiserToEnterService(usssalem), museumShip(usssalem), X@((museumShip(X) -> openToPublic(X))), (servedIn(usssalem,atlantic) /\ servedIn(usssalem,mediterranean)) --> openToPublic(usssalem)
```

## ARG-22 — True (FOLIO train example 39, story 14)

**Premises**

- The USS Salem is a heavy cruiser built for the United States Navy.  
  `HeavyCruiser(usssalem) ∧ BuiltFor(usssalem, unitedstatesnavy)`
- The last heavy cruiser to enter service was the USS Salem.  
  `LastHeavyCruiserToEnterService(usssalem)`
- The USS Salem is a museum ship.  
  `MuseumShip(usssalem)`
- Museum ships are open to the public.  
  `∀x (MuseumShip(x) → OpenToPublic(x))`
- The USS Salem served in the Atlantic and Mediterranean.  
  `ServedIn(usssalem, atlantic) ∧ ServedIn(usssalem, mediterranean)`

**Conclusion**

- There is a museum ship open to the public that served in the Mediterranean.  
  `∃x (MuseumShip(x) ∧ OpenToPublic(x) ∧ ServedIn(x, mediterranean))`

**Seqprover**

```
(heavyCruiser(usssalem) /\ builtFor(usssalem,unitedstatesnavy)), lastHeavyCruiserToEnterService(usssalem), museumShip(usssalem), X@((museumShip(X) -> openToPublic(X))), (servedIn(usssalem,atlantic) /\ servedIn(usssalem,mediterranean)) --> X#((museumShip(X) /\ (openToPublic(X) /\ servedIn(X,mediterranean))))
```

## ARG-23 — True (FOLIO train example 61, story 21)

**Premises**

- The Golden State Warriors are a team from San Francisco.  
  `Team(goldenStateWarriors) ∧ From(goldenStateWarriors, sanFrancisco)`
- The Golden State Warriors won the NBA finals.  
  `Won(goldenStateWarriors, nbaFinals)`
- All teams attending the NBA finals have won many games.  
  `∀x ((Team(x) ∧ Attending(x, nbaFinals)) → WonManyGames(x))`
- Boston Celtics are a team that lost the NBA finals.  
  `Team(bostonCeltics) ∧ Lost(bostonCeltics, nbaFinals)`
- If a team wins the NBA finals, then they will have more income.  
  `∀x ((Team(x) ∧ Won(x, nbaFinals)) → MoreIncome(x))`
- If a team wins or loses at the NBA finals, then they are attending the finals.  
  `∀x ((Won(x, nbaFinals) ∨ Lost(x, nbaFinals)) → Attending(x, nbaFinals))`

**Conclusion**

- The Boston Celtics have more than 30 years of experience.  
  `HasMoreThanThirtyYearsOfHistory(bostonCeltics)`

**Seqprover**

```
(team(goldenStateWarriors) /\ from(goldenStateWarriors,sanFrancisco)), won(goldenStateWarriors,nbaFinals), X@(((team(X) /\ attending(X,nbaFinals)) -> wonManyGames(X))), (team(bostonCeltics) /\ lost(bostonCeltics,nbaFinals)), X@(((team(X) /\ won(X,nbaFinals)) -> moreIncome(X))), X@(((won(X,nbaFinals) \/ lost(X,nbaFinals)) -> attending(X,nbaFinals))) --> hasMoreThanThirtyYearsOfHistory(bostonCeltics)
```

## ARG-24 — True (FOLIO train example 62, story 21)

**Premises**

- The Golden State Warriors are a team from San Francisco.  
  `Team(goldenStateWarriors) ∧ From(goldenStateWarriors, sanFrancisco)`
- The Golden State Warriors won the NBA finals.  
  `Won(goldenStateWarriors, nbaFinals)`
- All teams attending the NBA finals have won many games.  
  `∀x ((Team(x) ∧ Attending(x, nbaFinals)) → WonManyGames(x))`
- Boston Celtics are a team that lost the NBA finals.  
  `Team(bostonCeltics) ∧ Lost(bostonCeltics, nbaFinals)`
- If a team wins the NBA finals, then they will have more income.  
  `∀x ((Team(x) ∧ Won(x, nbaFinals)) → MoreIncome(x))`
- If a team wins or loses at the NBA finals, then they are attending the finals.  
  `∀x ((Won(x, nbaFinals) ∨ Lost(x, nbaFinals)) → Attending(x, nbaFinals))`

**Conclusion**

- The Golden State Warriors will have more income from gate receipts.  
  `MoreIncome(goldenStateWarriors)`

**Seqprover**

```
(team(goldenStateWarriors) /\ from(goldenStateWarriors,sanFrancisco)), won(goldenStateWarriors,nbaFinals), X@(((team(X) /\ attending(X,nbaFinals)) -> wonManyGames(X))), (team(bostonCeltics) /\ lost(bostonCeltics,nbaFinals)), X@(((team(X) /\ won(X,nbaFinals)) -> moreIncome(X))), X@(((won(X,nbaFinals) \/ lost(X,nbaFinals)) -> attending(X,nbaFinals))) --> moreIncome(goldenStateWarriors)
```

## ARG-25 — True (FOLIO train example 65, story 22)

**Premises**

- If a customer subscribes to AMC A-List, then he/she can watch 3 movies every week without any additional fees.  
  `∀x (SubscribedTo(x, aMCAList) → EligibleForThreeFreeMovies(x))`
- Some customers go to cinemas every week.  
  `∃x (CinemaEveryWeek(x))`
- Customers who prefer TV series will not watch TV series in cinemas.  
  `∀x (Prefer(x, tVSeries) → ¬WatchTVIn(x, cinemas))`
- James watches TV series in cinemas.  
  `WatchTVIn(james, cinemas)`
- James subscribes to AMC A-List.  
  `SubscribedTo(james, aMCAList)`
- Peter prefers TV series.  
  `Prefer(peter, tVSeries)`

**Conclusion**

- Peter will not watch TV series in cinemas.  
  `¬WatchTVIn(peter, cinemas)`

**Seqprover**

```
X@((subscribedTo(X,aMCAList) -> eligibleForThreeFreeMovies(X))), X#(cinemaEveryWeek(X)), X@((prefer(X,tVSeries) -> ~watchTVIn(X,cinemas))), watchTVIn(james,cinemas), subscribedTo(james,aMCAList), prefer(peter,tVSeries) --> ~watchTVIn(peter,cinemas)
```

## ARG-26 — True (FOLIO train example 67, story 23)

**Premises**

- All books written by Cixin Liu have sold more than 1 million copies.  
  `∀x ((Book(x) ∧ WrittenBy(x, cixinLiu)) → ∃y(MoreThan(y, oneMillion) ∧ Sold(x,y)))`
- Some books that have won the Hugo Award were written by Cixin Liu.  
  `∃x (Won(x, hugoAward) ∧ Book(x) ∧ WrittenBy(x, cixinLiu))`
- All books about the future are forward-looking.  
  `∀x ((Book(x) ∧ AboutFuture(x)) → FowardLooking(x))`
- The book Three-Body Problem has sold more than 1 million copies.  
  `Book(threeBodyProblem) ∧ ∃y(MoreThan(y, oneMillion) ∧ Sold(threeBodyProblem,y))`
- The Three-Body Problem is about the future.  
  `AboutFuture(threeBodyProblem)`

**Conclusion**

- The Three-Body Problem is forward-looking.  
  `AboutFuture(threeBodyProblem)`

**Seqprover**

```
X@(((book(X) /\ writtenBy(X,cixinLiu)) -> Y#((moreThan(Y,oneMillion) /\ sold(X,Y))))), X#((won(X,hugoAward) /\ (book(X) /\ writtenBy(X,cixinLiu)))), X@(((book(X) /\ aboutFuture(X)) -> fowardLooking(X))), (book(threeBodyProblem) /\ Y#((moreThan(Y,oneMillion) /\ sold(threeBodyProblem,Y)))), aboutFuture(threeBodyProblem) --> aboutFuture(threeBodyProblem)
```

## ARG-27 — True (FOLIO train example 101, story 35)

**Premises**

- An Olympian is a person who trains for an Olympic sport and goes to the Olympics.  
  `∀x ((DoesOlympicSport(x) ∧ GoesToOlympicGames(x)) → Olympian(x))`
- Carlos Reyes trains for an Olympic sport.  
  `DoesOlympicSport(carlosReyes)`
- Carlos Reyes went to the Olympics.  
  `GoesToOlympicGames(carlosReyes)`
- Carlos Reyes is a welterweight.  
  `WelterWeight(carlosReyes)`
- Heavy weights are not welterweights.  
  `∀x (WelterWeight(x) → ¬ HeavyWeight(x))`

**Conclusion**

- Carlos Reyes is an Olympian.  
  `Olympian(carlosReyes)`

**Seqprover**

```
X@(((doesOlympicSport(X) /\ goesToOlympicGames(X)) -> olympian(X))), doesOlympicSport(carlosReyes), goesToOlympicGames(carlosReyes), welterWeight(carlosReyes), X@((welterWeight(X) -> ~heavyWeight(X))) --> olympian(carlosReyes)
```

## ARG-28 — True (FOLIO train example 110, story 38)

**Premises**

- The Metropolitan Museum of Art is a museum in NYC.  
  `Museum(metropolitanMuseumOfArt) ∧ In(metropolitanMuseumOfArt, nYC)`
- Whitney Museum of American Art is a museum in NYC.  
  `Museum(whitneyMuseumOfAmericanArt) ∧ In(metropolitanMuseumOfArt, nYC)`
- The Museum of Modern Art (MoMA) is a museum in NYC.  
  `Museum(museumOfModernArt) ∧ In(museumOfModernArt, nYC)`
- The Metropolitan Museum of Art includes Byzantine and Islamic Art.  
  `Include(metropolitanMuseumOfArt, byzantineArt) ∧ Include(metropolitanMuseumOfArt, islamicArt)`
- Whitney Museum of American Art includes American art.  
  `Include(whitneyMuseumOfAmericanArt, americanArt)`

**Conclusion**

- A museum in NYC includes Byzantine and Islamic Art.  
  `∃x (Museum(x) ∧ In(x, nYC) ∧ Include(x, byzantineArt) ∧ Include(x, islamicArt))`

**Seqprover**

```
(museum(metropolitanMuseumOfArt) /\ in(metropolitanMuseumOfArt,nYC)), (museum(whitneyMuseumOfAmericanArt) /\ in(metropolitanMuseumOfArt,nYC)), (museum(museumOfModernArt) /\ in(museumOfModernArt,nYC)), (include(metropolitanMuseumOfArt,byzantineArt) /\ include(metropolitanMuseumOfArt,islamicArt)), include(whitneyMuseumOfAmericanArt,americanArt) --> X#((museum(X) /\ (in(X,nYC) /\ (include(X,byzantineArt) /\ include(X,islamicArt)))))
```

## ARG-29 — True (FOLIO train example 111, story 38)

**Premises**

- The Metropolitan Museum of Art is a museum in NYC.  
  `Museum(metropolitanMuseumOfArt) ∧ In(metropolitanMuseumOfArt, nYC)`
- Whitney Museum of American Art is a museum in NYC.  
  `Museum(whitneyMuseumOfAmericanArt) ∧ In(metropolitanMuseumOfArt, nYC)`
- The Museum of Modern Art (MoMA) is a museum in NYC.  
  `Museum(museumOfModernArt) ∧ In(museumOfModernArt, nYC)`
- The Metropolitan Museum of Art includes Byzantine and Islamic Art.  
  `Include(metropolitanMuseumOfArt, byzantineArt) ∧ Include(metropolitanMuseumOfArt, islamicArt)`
- Whitney Museum of American Art includes American art.  
  `Include(whitneyMuseumOfAmericanArt, americanArt)`

**Conclusion**

- A museum in NYC includes American art.  
  `∃x (Museum(x) ∧ In(x, nYC) ∧ Include(x, americanArt))`

**Seqprover**

```
(museum(metropolitanMuseumOfArt) /\ in(metropolitanMuseumOfArt,nYC)), (museum(whitneyMuseumOfAmericanArt) /\ in(metropolitanMuseumOfArt,nYC)), (museum(museumOfModernArt) /\ in(museumOfModernArt,nYC)), (include(metropolitanMuseumOfArt,byzantineArt) /\ include(metropolitanMuseumOfArt,islamicArt)), include(whitneyMuseumOfAmericanArt,americanArt) --> X#((museum(X) /\ (in(X,nYC) /\ include(X,americanArt))))
```

## ARG-30 — True (FOLIO train example 119, story 41)

**Premises**

- Federico Garcia Lorca was a talented Spanish poet, and he supported the Popular Front.  
  `TalentedPoet(lorca) ∧ Support(lorca, populists)`
- The Spanish Nationalists opposed anyone who supported the Popular Front  
  `∀x (Support(x, populists) → Opposed(nationalists, x))`
- Talented poets are popular.  
  `∀x (TalentedPoet(x) → Popular(x))`
- Spanish Nationalists killed anyone who they opposed and who was popular.  
  `∀x ((Opposed(nationalists, x) ∧ Popular(x)) → Killed(nationalists, x))`
- Daniel supported the Popular Front but was not popular.  
  `Support(daniel, populists) ∧ (¬Popular(daniel))`

**Conclusion**

- The Spanish Nationalists killed Lorca.  
  `Killed(nationalists, lorca)`

**Seqprover**

```
(talentedPoet(lorca) /\ support(lorca,populists)), X@((support(X,populists) -> opposed(nationalists,X))), X@((talentedPoet(X) -> popular(X))), X@(((opposed(nationalists,X) /\ popular(X)) -> killed(nationalists,X))), (support(daniel,populists) /\ ~popular(daniel)) --> killed(nationalists,lorca)
```

## ARG-31 — False (FOLIO validation example 1, story 0)

**Premises**

- There are six types of wild turkeys: Eastern wild turkey, Osceola wild turkey, Gould’s wild turkey, Merriam’s wild turkey, Rio Grande wild turkey, and Ocellated wild turkey.  
  `∀x (WildTurkey(x) → (EasternWildTurkey(x) ∨ OsceolaWildTurkey(x) ∨ GouldsWildTurkey(x) ∨ MerriamsWildTurkey(x) ∨ RiograndeWildTurkey(x) ∨ OcellatedWildTurkey(x)))`
- Tom is not an Eastern wild turkey.  
  `¬(EasternWildTurkey(tom))`
- Tom is not an Osceola wild turkey.  
  `¬(OsceolaWildTurkey(tom))`
- Tom is not a Gould's wild turkey.  
  `¬(GouldsWildTurkey(tom))`
- Tom is neither a Merriam's wild turkey nor a Rio Grande wild turkey.  
  `¬(MerriamsWildTurkey(tom) ∨ RiograndeWildTurkey(tom))`
- Tom is a wild turkey.  
  `WildTurkey(tom)`

**Conclusion**

- Tom is an Eastern wild turkey.  
  `EasternWildTurkey(tom)`

**Seqprover**

```
X@((wildTurkey(X) -> (easternWildTurkey(X) \/ (osceolaWildTurkey(X) \/ (gouldsWildTurkey(X) \/ (merriamsWildTurkey(X) \/ (riograndeWildTurkey(X) \/ ocellatedWildTurkey(X)))))))), ~easternWildTurkey(tom), ~osceolaWildTurkey(tom), ~gouldsWildTurkey(tom), ~(merriamsWildTurkey(tom) \/ riograndeWildTurkey(tom)), wildTurkey(tom) --> easternWildTurkey(tom)
```

## ARG-32 — False (FOLIO validation example 254, story 83)

**Premises**

- All vehicle registration plates in Istanbul begin with the number 34.  
  `∀x (VehicleRegistrationPlateIn(x, istanbul) → BeginWith(x, num34))`
- Plates that do not begin with the number 34 are not from Istanbul.  
  `∀x (¬BeginWith(x, num34) → ¬FromIstanbul(x))`
- Joe's vehicle registration plate is from Istanbul.  
  `∃x (Owns(joe, x) ∧ VehicleRegistrationPlateIn(x, istanbul))`
- Tom's license plate begins with the number 35.  
  `∃x (Owns(tom, x) ∧ BeginWith(x, num35))`
- If a license plate begins with the number 35, then it does not begin with the number 34.  
  `∀x (BeginWith(x, num35) → ¬BeginWith(x, num34))`

**Conclusion**

- Tom's license plate is from Istanbul.  
  `∃x (Owns(tom, x) ∧ VehicleRegistrationPlateIn(x, istanbul))`

**Seqprover**

```
X@((vehicleRegistrationPlateIn(X,istanbul) -> beginWith(X,num34))), X@((~beginWith(X,num34) -> ~fromIstanbul(X))), X#((owns(joe,X) /\ vehicleRegistrationPlateIn(X,istanbul))), X#((owns(tom,X) /\ beginWith(X,num35))), X@((beginWith(X,num35) -> ~beginWith(X,num34))) --> X#((owns(tom,X) /\ vehicleRegistrationPlateIn(X,istanbul)))
```

## ARG-33 — False (FOLIO validation example 304, story 101)

**Premises**

- Ailton Silva, born in 1995, is commonly known as Ailton.  
  `BornIn(ailtonSilva, year1995) ∧ CommonlyKnownAs(ailtonSilva, ailton)`
- Ailton is a football player who was loaned out to Braga.  
  `FootballPlayer(ailton) ∧ LoanedTo(ailton, braga)`
- Ailton Silva is a Brazilian footballer who plays for Náutico.  
  `Brazilian(ailtonSilva) ∧ Footballplayer(ailtonSilva) ∧ PlayFor(ailtonSilva, nautico)`
- Náutico is a football club along with Braga.  
  `FootballClub(nautico) ∧ FootballClub(braga)`
- Fluminense is a football club.  
  `FootballClub(fluminense)`

**Conclusion**

- No one playing for Nautico is Brazilian.  
  `∀x (PlayFor(x, nautico) → ¬Brazilian(x))`

**Seqprover**

```
(bornIn(ailtonSilva,year1995) /\ commonlyKnownAs(ailtonSilva,ailton)), (footballPlayer(ailton) /\ loanedTo(ailton,braga)), (brazilian(ailtonSilva) /\ (footballplayer(ailtonSilva) /\ playFor(ailtonSilva,nautico))), (footballClub(nautico) /\ footballClub(braga)), footballClub(fluminense) --> X@((playFor(X,nautico) -> ~brazilian(X)))
```

## ARG-34 — False (FOLIO validation example 305, story 101)

**Premises**

- Ailton Silva, born in 1995, is commonly known as Ailton.  
  `BornIn(ailtonSilva, year1995) ∧ CommonlyKnownAs(ailtonSilva, ailton)`
- Ailton is a football player who was loaned out to Braga.  
  `FootballPlayer(ailton) ∧ LoanedTo(ailton, braga)`
- Ailton Silva is a Brazilian footballer who plays for Náutico.  
  `Brazilian(ailtonSilva) ∧ Footballplayer(ailtonSilva) ∧ PlayFor(ailtonSilva, nautico)`
- Náutico is a football club along with Braga.  
  `FootballClub(nautico) ∧ FootballClub(braga)`
- Fluminense is a football club.  
  `FootballClub(fluminense)`

**Conclusion**

- Ailton Silva does not play for a football club.  
  `∀x (FootballClub(x) → ¬PlayFor(ailtonSilva, x))`

**Seqprover**

```
(bornIn(ailtonSilva,year1995) /\ commonlyKnownAs(ailtonSilva,ailton)), (footballPlayer(ailton) /\ loanedTo(ailton,braga)), (brazilian(ailtonSilva) /\ (footballplayer(ailtonSilva) /\ playFor(ailtonSilva,nautico))), (footballClub(nautico) /\ footballClub(braga)), footballClub(fluminense) --> X@((footballClub(X) -> ~playFor(ailtonSilva,X)))
```

## ARG-35 — False (FOLIO validation example 306, story 101)

**Premises**

- Ailton Silva, born in 1995, is commonly known as Ailton.  
  `BornIn(ailtonSilva, year1995) ∧ CommonlyKnownAs(ailtonSilva, ailton)`
- Ailton is a football player who was loaned out to Braga.  
  `FootballPlayer(ailton) ∧ LoanedTo(ailton, braga)`
- Ailton Silva is a Brazilian footballer who plays for Náutico.  
  `Brazilian(ailtonSilva) ∧ Footballplayer(ailtonSilva) ∧ PlayFor(ailtonSilva, nautico)`
- Náutico is a football club along with Braga.  
  `FootballClub(nautico) ∧ FootballClub(braga)`
- Fluminense is a football club.  
  `FootballClub(fluminense)`

**Conclusion**

- Ailton was not loaned out to a football club.  
  `∀x (FootballClub(x) → ¬LoanedTo(ailton, x))`

**Seqprover**

```
(bornIn(ailtonSilva,year1995) /\ commonlyKnownAs(ailtonSilva,ailton)), (footballPlayer(ailton) /\ loanedTo(ailton,braga)), (brazilian(ailtonSilva) /\ (footballplayer(ailtonSilva) /\ playFor(ailtonSilva,nautico))), (footballClub(nautico) /\ footballClub(braga)), footballClub(fluminense) --> X@((footballClub(X) -> ~loanedTo(ailton,X)))
```

## ARG-36 — False (FOLIO validation example 389, story 131)

**Premises**

- Machine Learning algorithms can be categorized as supervised learning, unsupervised learning, and reinforcement learning.  
  `∀x (MachineLearningAlgorithm(x) → SupervisedLearningAlgorithm(x) ∨ UnsupervisedLearningAlgorithm(x) ∨ ReinforcementLearningAlgorithm(x))`
- Unsupervised learning algorithms do not require labeled data.  
  `∀x (UnsupervisedLearningAlgorithm(x) → ¬Require(x, labeledData))`
- The state-of-the-art text summarization model is trained with machine learning algorithms.  
  `∀x (TrainedWith(stateOfTheArtTextSummarizationModel, x) → MachineLearningAlgorithm(x))`
- Reinforcement learning is not used to train the state-of-the-art text summarization model.  
  `∀x (ReinforcementLearningAlgorithm(x) → ¬TrainedWith(stateOfTheArtTextSummarizationModel, x))`
- The Machine Learning algorithm for training text summarization models requires labeled data.  
  `∀x ((MachineLearningAlgorithm(x) ∧ TrainedWith(stateOfTheArtTextSummarizationModel, x)) → Require(x, labeledData))`

**Conclusion**

- Unsupervised learning is used to train the state-of-the-art text summarization model.  
  `∃x (UnsupervisedLearningAlgorithm(x) ∧ TrainedWith(stateOfTheArtTextSummarizationModel, x))`

**Seqprover**

```
X@((machineLearningAlgorithm(X) -> (supervisedLearningAlgorithm(X) \/ (unsupervisedLearningAlgorithm(X) \/ reinforcementLearningAlgorithm(X))))), X@((unsupervisedLearningAlgorithm(X) -> ~require(X,labeledData))), X@((trainedWith(stateOfTheArtTextSummarizationModel,X) -> machineLearningAlgorithm(X))), X@((reinforcementLearningAlgorithm(X) -> ~trainedWith(stateOfTheArtTextSummarizationModel,X))), X@(((machineLearningAlgorithm(X) /\ trainedWith(stateOfTheArtTextSummarizationModel,X)) -> require(X,labeledData))) --> X#((unsupervisedLearningAlgorithm(X) /\ trainedWith(stateOfTheArtTextSummarizationModel,X)))
```

## ARG-37 — False (FOLIO validation example 441, story 151)

**Premises**

- Barutin Cove is a cove named after the Bulgarian settlement of Barutin.  
  `Cove(barutinCove) ∧ NamedAfter(barutinCove, barutinSettlement) ∧ LocatedIn(barutinSettlement, bulgaria)`
- Barutin Cove is on the southwest coast of Snow Island.  
  `LocatedIn(barutinCove, snowIsland)`
- Snow Island, Greenwich Island, and Deception Island are located in the South Shetland Islands.  
  `LocatedIn(snowIsland, southShetlandIslands) ∧ LocatedIn(greenwichIsland, southShetlandIslands) ∧ LocatedIn(deceptionIsland, southShetlandIslands)`
- Antarctica is located on the South Shetland Islands.  
  `LocatedIn(southShetlandIslands, antarctica)`
- If place A is located in place B and place B is located in place C, then place A is located in place C.  
  `∀x ∀y ∀z ((LocatedIn(x, y) ∧ LocatedIn(y, z)) → LocatedIn(x, z))`

**Conclusion**

- Barutin Cove is not located in Antarctica.  
  `¬LocatedIn(barutinCove, antarctica)`

**Seqprover**

```
(cove(barutinCove) /\ (namedAfter(barutinCove,barutinSettlement) /\ locatedIn(barutinSettlement,bulgaria))), locatedIn(barutinCove,snowIsland), (locatedIn(snowIsland,southShetlandIslands) /\ (locatedIn(greenwichIsland,southShetlandIslands) /\ locatedIn(deceptionIsland,southShetlandIslands))), locatedIn(southShetlandIslands,antarctica), X@(Y@(Z@(((locatedIn(X,Y) /\ locatedIn(Y,Z)) -> locatedIn(X,Z))))) --> ~locatedIn(barutinCove,antarctica)
```

## ARG-38 — False (FOLIO validation example 562, story 197)

**Premises**

- It costs $205 to take the GRE test, which is cheaper than $300.  
  `Cost(gRE, 205) ∧ Cheaper(205, 300)`
- ETS provides financial aid to those GRE applicants who prove economic hardship.  
  `∀x (ApplicantOf(x, gre) ∧ Prove(x, economicHardship) → ProvideTo(ets, financialAid, x))`
- Those living in single-parent families or having few resources available to them can prove economic hardship.  
  `∀x (LivingIn(x, singleParentFamily) ∨ AvailableTo(fewResources, x) → Prove(x, economicHardship))`
- Tom lives in a single-parent family.  
  `LivingIn(tom, singleParentFamily)`
- Tom's dad has been out of work, and Tom has few resources available to them.  
  `OutOfWork(tomsDad) ∧ AvailableTo(fewResources, tom)`
- Tom is applying to take the GRE test.  
  `ApplicantOf(tom, gre)`

**Conclusion**

- No one taking the GRE test has financial aid provided to them by something.  
  `¬(∃x ∃y (Applicant(x, gRE) ∧ ProvidesFinancialAidTo(y, x)))`

**Seqprover**

```
(cost(gRE,205) /\ cheaper(205,300)), X@(((applicantOf(X,gre) /\ prove(X,economicHardship)) -> provideTo(ets,financialAid,X))), X@(((livingIn(X,singleParentFamily) \/ availableTo(fewResources,X)) -> prove(X,economicHardship))), livingIn(tom,singleParentFamily), (outOfWork(tomsDad) /\ availableTo(fewResources,tom)), applicantOf(tom,gre) --> ~X#(Y#((applicant(X,gRE) /\ providesFinancialAidTo(Y,X))))
```

## ARG-39 — False (FOLIO validation example 580, story 203)

**Premises**

- Plungers suck.  
  `∀x (Plunger(x) → Suck(x))`
- Vacuums suck.  
  `∀x (Vacuum(x) → Suck(x))`
- Vampires suck.  
  `∀x (Vampire(x) → Suck(x))`
- Space is a vacuum.  
  `Vacuum(space)`
- A duster is a household appliance that doesn't suck.  
  `HouseholdAppliance(duster) ∧ ¬Suck(duster)`

**Conclusion**

- If something is a household appliance, it sucks.  
  `∀x (HouseHoldApp(x) → Suck(x))`

**Seqprover**

```
X@((plunger(X) -> suck(X))), X@((vacuum(X) -> suck(X))), X@((vampire(X) -> suck(X))), vacuum(space), (householdAppliance(duster) /\ ~suck(duster)) --> X@((houseHoldApp(X) -> suck(X)))
```

## ARG-40 — False (FOLIO validation example 608, story 213)

**Premises**

- All Romance languages are Indo-European languages.  
  `∀x (RomanceLanguage(x) → IndoEuropeanLanguage(x))`
- Romance languages are a language family.  
  `∀x (RomanceLanguage(x) → MemberOf(x, languageFamily))`
- All languages within a language family are related to each other.  
  `∀x ∀y ∀z ((MemberOf(x, z) ∧ MemberOf(y, z)) → (Related(x, y) ∧ Related(y, x)))`
- French and Spanish are both Romance languages.  
  `RomanceLanguage(french) ∧ RomanceLanguage(spanish)`
- German is related to Spanish.  
  `Related(german, spanish)`
- Basque is not related to any other language.  
  `∀x (Language(x) → ¬Related(basque, x))`

**Conclusion**

- Basque is a Romance language.  
  `RomanceLanguage(basque)`

**Seqprover**

```
X@((romanceLanguage(X) -> indoEuropeanLanguage(X))), X@((romanceLanguage(X) -> memberOf(X,languageFamily))), X@(Y@(Z@(((memberOf(X,Z) /\ memberOf(Y,Z)) -> (related(X,Y) /\ related(Y,X)))))), (romanceLanguage(french) /\ romanceLanguage(spanish)), related(german,spanish), X@((language(X) -> ~related(basque,X))) --> romanceLanguage(basque)
```

## ARG-41 — False (FOLIO validation example 805, story 319)

**Premises**

- No baked sweets are spicy.  
  `∀x (BakedSweet(x) → ¬Spicy(x))`
- All cupcakes are baked sweets.  
  `∀x (Cupcake(x) → BakedSweet(x))`
- All mala hotpots are spicy.  
  `∀x (MalaHotpot(x) → Spicy(x))`
- All products from Baked by Melissa are cupcakes.  
  `∀x (Product(x) ∧ From(x, bakedByMelissa) → Cupcake(x))`
- Dried Thai chilies are spicy or mala hotpots or not baked sweets.  
  `Spicy(driedThaiChili) ∨ MalaHotpot(driedThaiChili)∨ ¬BakedSweet(driedThaiChili)`

**Conclusion**

- Dried Thai chilies are products of Baked by Melissa.  
  `Product(driedThaiChili) ∧ From(driedThaiChili, bakedByMelissa)`

**Seqprover**

```
X@((bakedSweet(X) -> ~spicy(X))), X@((cupcake(X) -> bakedSweet(X))), X@((malaHotpot(X) -> spicy(X))), X@(((product(X) /\ from(X,bakedByMelissa)) -> cupcake(X))), (spicy(driedThaiChili) \/ (malaHotpot(driedThaiChili) \/ ~bakedSweet(driedThaiChili))) --> (product(driedThaiChili) /\ from(driedThaiChili,bakedByMelissa))
```

## ARG-42 — False (FOLIO validation example 934, story 352)

**Premises**

- All business organizations are legal entities.  
  `∀x (BusinessOrganization(x) → LegalEntity(x))`
- All companies are business organizations.  
  `∀x (Company(x) → BusinessOrganization(x))`
- All private companies are companies.  
  `∀x (PrivateCompany(x) → Company(x))`
- All legal entities are created under law.  
  `∀x (LegalEntity(x) → CreatedUnderLaw(x))`
- All legal entities have legal obligations.  
  `∀x (LegalEntity(x) → LegalObligation(x))`
- If the Harvard Weekly Book Club is created under law, then it is not a private company.  
  `CreatedUnderLaw(harvardWeeklyBookClub) → ¬PrivateCompany(harvardWeeklyBookClub)`

**Conclusion**

- The Harvard Weekly Book club has legal obligations and is a private company.  
  `LegalObligation(harvardWeeklyBookClub) ∧ PrivateCompany(harvardWeeklyBookClub)`

**Seqprover**

```
X@((businessOrganization(X) -> legalEntity(X))), X@((company(X) -> businessOrganization(X))), X@((privateCompany(X) -> company(X))), X@((legalEntity(X) -> createdUnderLaw(X))), X@((legalEntity(X) -> legalObligation(X))), (createdUnderLaw(harvardWeeklyBookClub) -> ~privateCompany(harvardWeeklyBookClub)) --> (legalObligation(harvardWeeklyBookClub) /\ privateCompany(harvardWeeklyBookClub))
```

## ARG-43 — False (FOLIO validation example 1034, story 386)

**Premises**

- If something is a deadly disease, then it comes with a low survival rate.  
  `∀x (DeadlyDiseases(x) → ComeWith(x, lowSurvivalRate))`
- Severe cancers are deadly diseases.  
  `∀x (SevereCancer(x) → DeadlyDiseases(x))`
- Bile duct cancer is a severe form cancer.  
  `∀x (BileDuctCancer(x) → SevereCancer(x))`
- All Cholangiocarcinoma is bile duct cancer.  
  `∀x (Cholangiocarcinoma(x) → BileDuctCancer(x))`
- Mild flu comes with a low survival rate.  
  `∀x (MildFlu(x) → ¬ComeWith(x, lowSurvivalRate))`
- Colorectal cancer is not both a bile duct cancer and with a low survival rate.  
  `¬(BileDuctCancer(colorectalCancer) ∧ ComeWith(colorectalCancer, lowSurvivalRate))`

**Conclusion**

- Colorectal cancer is a form of Cholangiocarcinoma and it is a kind of mild flu or a kind of bile duct cancer, or all of the above.  
  `Cholangiocarcinoma(colorectalCancer) ∧ (MildFlu(colorectalCancer) ∨ BileDuctCancer(colorectalCancer))`

**Seqprover**

```
X@((deadlyDiseases(X) -> comeWith(X,lowSurvivalRate))), X@((severeCancer(X) -> deadlyDiseases(X))), X@((bileDuctCancer(X) -> severeCancer(X))), X@((cholangiocarcinoma(X) -> bileDuctCancer(X))), X@((mildFlu(X) -> ~comeWith(X,lowSurvivalRate))), ~(bileDuctCancer(colorectalCancer) /\ comeWith(colorectalCancer,lowSurvivalRate)) --> (cholangiocarcinoma(colorectalCancer) /\ (mildFlu(colorectalCancer) \/ bileDuctCancer(colorectalCancer)))
```

## ARG-44 — False (FOLIO validation example 1272, story 442)

**Premises**

- All Brown Swiss cattle are cows.  
  `∀x (BrownSwissCattle(x) → Cow(x))`
- Some pets are Brown Swiss Cattle.  
  `∃x (Pet(x) ∧ BrownSwissCattle(x))`
- All cows are domesticated animals.  
  `∀x (Cow(x) → DomesticatedAnimal(x))`
- Alligators are not domesticated animals.  
  `∀x (Aligator(x) → ¬DomesticatedAnimal(x))`
- Ted is an alligator.  
  `Aligator(ted)`

**Conclusion**

- Ted is a pet and Brown Swiss cattle  
  `Pet(ted) ∧ BrownSwissCattle(ted)`

**Seqprover**

```
X@((brownSwissCattle(X) -> cow(X))), X#((pet(X) /\ brownSwissCattle(X))), X@((cow(X) -> domesticatedAnimal(X))), X@((aligator(X) -> ~domesticatedAnimal(X))), aligator(ted) --> (pet(ted) /\ brownSwissCattle(ted))
```

## ARG-45 — False (FOLIO validation example 1315, story 456)

**Premises**

- Some professional basketball players are not American nationals.  
  `∃x (Professional(x) ∧ BasketballPlayer(x) ∧ ¬AmericanNational(x))`
- All professional basketball players can do jump shots.  
  `∀x (Professional(x) ∧ BasketballPlayer(x) → CanDo(x, jumpShot))`
- If someone can jump shots, they leap straight into the air.  
  `∀x (CanDo(x, jumpShot) → LeapStraightIntoAir(x))`
- If someone leaps straight into the air, they activate their leg muscles.  
  `∀x (LeapStraightIntoAir(x) → Activate(x, legMuscle))`
- Yuri does not activate his leg muscles.  
  `¬Activate(yuri, legMuscle)`

**Conclusion**

- Yuri is an American professional basketball player.  
  `AmericanNational(yuri) ∧ Professional(yuri) ∧ BasketballPlayer(yuri)`

**Seqprover**

```
X#((professional(X) /\ (basketballPlayer(X) /\ ~americanNational(X)))), X@(((professional(X) /\ basketballPlayer(X)) -> canDo(X,jumpShot))), X@((canDo(X,jumpShot) -> leapStraightIntoAir(X))), X@((leapStraightIntoAir(X) -> activate(X,legMuscle))), ~activate(yuri,legMuscle) --> (americanNational(yuri) /\ (professional(yuri) /\ basketballPlayer(yuri)))
```

## ARG-46 — False (FOLIO validation example 1316, story 456)

**Premises**

- Some professional basketball players are not American nationals.  
  `∃x (Professional(x) ∧ BasketballPlayer(x) ∧ ¬AmericanNational(x))`
- All professional basketball players can do jump shots.  
  `∀x (Professional(x) ∧ BasketballPlayer(x) → CanDo(x, jumpShot))`
- If someone can jump shots, they leap straight into the air.  
  `∀x (CanDo(x, jumpShot) → LeapStraightIntoAir(x))`
- If someone leaps straight into the air, they activate their leg muscles.  
  `∀x (LeapStraightIntoAir(x) → Activate(x, legMuscle))`
- Yuri does not activate his leg muscles.  
  `¬Activate(yuri, legMuscle)`

**Conclusion**

- If Yuri does not leap straight into the air, then Yuri is an American professional basketball player.  
  `¬LeapStraightIntoAir(yuri) → (AmericanNational(yuri) ∧ Professional(yuri) ∧ BasketballPlayer(yuri))`

**Seqprover**

```
X#((professional(X) /\ (basketballPlayer(X) /\ ~americanNational(X)))), X@(((professional(X) /\ basketballPlayer(X)) -> canDo(X,jumpShot))), X@((canDo(X,jumpShot) -> leapStraightIntoAir(X))), X@((leapStraightIntoAir(X) -> activate(X,legMuscle))), ~activate(yuri,legMuscle) --> (~leapStraightIntoAir(yuri) -> (americanNational(yuri) /\ (professional(yuri) /\ basketballPlayer(yuri))))
```

## ARG-47 — False (FOLIO train example 19, story 7)

**Premises**

- Six, seven and eight are real numbers.  
  `RealNum(num6) ∧ RealNum(num7) ∧ RealNum(num8)`
- If a real number equals another real number added by one, the first number is larger.  
  `∀x ∀y ((RealNum(x) ∧ RealNum(y) ∧ IsSuccessorOf(x, y)) → Larger(x, y))`
- If the number x is larger than the number y, then y is not larger than x.  
  `∀x ∀y (Larger(x, y) → ¬Larger(y, x))`
- Seven equals six plus one.  
  `∃y(IsSuccessorOf(y, num6) ∧ Equals(num7, y))`
- Eight equals seven plus one.  
  `∃y(IsSuccessorOf(y, num7) ∧ Equals(num8, y))`
- Two is positive.  
  `Positive(num2)`
- If a number is positive, then the double of it is also positive.  
  `∀x ∀y ((Positive(x) ∧ IsDouble(y, x)) → Positive(y))`
- Eight is the double of four.  
  `IsDouble(num8, num4)`
- Four is the double of two.  
  `IsDouble(num4, num2)`

**Conclusion**

- Six is larger than seven.  
  `Larger(six, seven)`

**Seqprover**

```
(realNum(num6) /\ (realNum(num7) /\ realNum(num8))), X@(Y@(((realNum(X) /\ (realNum(Y) /\ isSuccessorOf(X,Y))) -> larger(X,Y)))), X@(Y@((larger(X,Y) -> ~larger(Y,X)))), Y#((isSuccessorOf(Y,num6) /\ equals(num7,Y))), Y#((isSuccessorOf(Y,num7) /\ equals(num8,Y))), positive(num2), X@(Y@(((positive(X) /\ isDouble(Y,X)) -> positive(Y)))), isDouble(num8,num4), isDouble(num4,num2) --> larger(six,seven)
```

## ARG-48 — False (FOLIO train example 37, story 13)

**Premises**

- System 7 is a UK-based electronic dance music band.  
  `BasedIn(system7, uk) ∧ ElectronicDanceMusicBand(system7)`
- Steve Hillage and Miquette Giraudy formed System 7.  
  `Form(stevehillage, system7) ∧ Form(miquettegiraudy, system7)`
- Steve Hillage and Miquette Giraudy are former members of the band Gong.  
  `FormerMemberOf(stevehillage, gong) ∧ FormerMemberOf(miquettegiraudy, gong)`
- Electric dance music bands are bands.  
  `∀x (ElectronicDanceMusicBand(x) → Band(x))`
- System 7 has released several club singles.  
  `∃x (ClubSingle(x) ∧ Release(system7, x))`
- Club singles are not singles.  
  `∀x (ClubSingle(x) → ¬Single(x))`

**Conclusion**

- System 7 is not a band.  
  `¬Band(system7)`

**Seqprover**

```
(basedIn(system7,uk) /\ electronicDanceMusicBand(system7)), (form(stevehillage,system7) /\ form(miquettegiraudy,system7)), (formerMemberOf(stevehillage,gong) /\ formerMemberOf(miquettegiraudy,gong)), X@((electronicDanceMusicBand(X) -> band(X))), X#((clubSingle(X) /\ release(system7,X))), X@((clubSingle(X) -> ~single(X))) --> ~band(system7)
```

## ARG-49 — False (FOLIO train example 40, story 14)

**Premises**

- The USS Salem is a heavy cruiser built for the United States Navy.  
  `HeavyCruiser(usssalem) ∧ BuiltFor(usssalem, unitedstatesnavy)`
- The last heavy cruiser to enter service was the USS Salem.  
  `LastHeavyCruiserToEnterService(usssalem)`
- The USS Salem is a museum ship.  
  `MuseumShip(usssalem)`
- Museum ships are open to the public.  
  `∀x (MuseumShip(x) → OpenToPublic(x))`
- The USS Salem served in the Atlantic and Mediterranean.  
  `ServedIn(usssalem, atlantic) ∧ ServedIn(usssalem, mediterranean)`

**Conclusion**

- The USS Salem was not the last heavy cruiser to enter service.  
  `¬LastHeavyCruiserToEnterService(usssalem)`

**Seqprover**

```
(heavyCruiser(usssalem) /\ builtFor(usssalem,unitedstatesnavy)), lastHeavyCruiserToEnterService(usssalem), museumShip(usssalem), X@((museumShip(X) -> openToPublic(X))), (servedIn(usssalem,atlantic) /\ servedIn(usssalem,mediterranean)) --> ~lastHeavyCruiserToEnterService(usssalem)
```

## ARG-50 — False (FOLIO train example 63, story 22)

**Premises**

- If a customer subscribes to AMC A-List, then he/she can watch 3 movies every week without any additional fees.  
  `∀x (SubscribedTo(x, aMCAList) → EligibleForThreeFreeMovies(x))`
- Some customers go to cinemas every week.  
  `∃x (CinemaEveryWeek(x))`
- Customers who prefer TV series will not watch TV series in cinemas.  
  `∀x (Prefer(x, tVSeries) → ¬WatchTVIn(x, cinemas))`
- James watches TV series in cinemas.  
  `WatchTVIn(james, cinemas)`
- James subscribes to AMC A-List.  
  `SubscribedTo(james, aMCAList)`
- Peter prefers TV series.  
  `Prefer(peter, tVSeries)`

**Conclusion**

- James cannot watch 3 movies every week without any additional fees.  
  `¬EligibleForThreeFreeMovies(james)`

**Seqprover**

```
X@((subscribedTo(X,aMCAList) -> eligibleForThreeFreeMovies(X))), X#(cinemaEveryWeek(X)), X@((prefer(X,tVSeries) -> ~watchTVIn(X,cinemas))), watchTVIn(james,cinemas), subscribedTo(james,aMCAList), prefer(peter,tVSeries) --> ~eligibleForThreeFreeMovies(james)
```

## ARG-51 — False (FOLIO train example 102, story 35)

**Premises**

- An Olympian is a person who trains for an Olympic sport and goes to the Olympics.  
  `∀x ((DoesOlympicSport(x) ∧ GoesToOlympicGames(x)) → Olympian(x))`
- Carlos Reyes trains for an Olympic sport.  
  `DoesOlympicSport(carlosReyes)`
- Carlos Reyes went to the Olympics.  
  `GoesToOlympicGames(carlosReyes)`
- Carlos Reyes is a welterweight.  
  `WelterWeight(carlosReyes)`
- Heavy weights are not welterweights.  
  `∀x (WelterWeight(x) → ¬ HeavyWeight(x))`

**Conclusion**

- Carlos Reyes is a heavy weight.  
  `HeavyWeight(carlosReyes)`

**Seqprover**

```
X@(((doesOlympicSport(X) /\ goesToOlympicGames(X)) -> olympian(X))), doesOlympicSport(carlosReyes), goesToOlympicGames(carlosReyes), welterWeight(carlosReyes), X@((welterWeight(X) -> ~heavyWeight(X))) --> heavyWeight(carlosReyes)
```

## ARG-52 — False (FOLIO train example 178, story 60)

**Premises**

- All buildings in New Haven are not high.  
  `∀x (In(x, newHaven) → ¬High(x))`
- All buildings managed by Yale Housing are located in New Haven.  
  `∀x (YaleHousing(x) → In(x, newHaven))`
- All buildings in Manhattans are high.  
  `∀x (In(x, manhattan) → High(x))`
- All buildings owned by Bloomberg are located in Manhattans.  
  `∀x (Bloomberg(x) → In(x, manhattan))`
- All buildings with the Bloomberg logo are owned by Bloomberg.  
  `∀x (BloombergLogo(x) → Bloomberg(x))`
- Tower A is managed by Yale Housing.  
  `YaleHousing(tower-a)`
- Tower B is with the Bloomberg logo.  
  `BloombergLogo(tower-b)`

**Conclusion**

- Tower B is not located in Manhattans.  
  `¬In(tower-b, manhattan)`

**Seqprover**

```
X@((in(X,newHaven) -> ~high(X))), X@((yaleHousing(X) -> in(X,newHaven))), X@((in(X,manhattan) -> high(X))), X@((bloomberg(X) -> in(X,manhattan))), X@((bloombergLogo(X) -> bloomberg(X))), yaleHousing('tower-a'), bloombergLogo('tower-b') --> ~in('tower-b',manhattan)
```

## ARG-53 — False (FOLIO train example 179, story 60)

**Premises**

- All buildings in New Haven are not high.  
  `∀x (In(x, newHaven) → ¬High(x))`
- All buildings managed by Yale Housing are located in New Haven.  
  `∀x (YaleHousing(x) → In(x, newHaven))`
- All buildings in Manhattans are high.  
  `∀x (In(x, manhattan) → High(x))`
- All buildings owned by Bloomberg are located in Manhattans.  
  `∀x (Bloomberg(x) → In(x, manhattan))`
- All buildings with the Bloomberg logo are owned by Bloomberg.  
  `∀x (BloombergLogo(x) → Bloomberg(x))`
- Tower A is managed by Yale Housing.  
  `YaleHousing(tower-a)`
- Tower B is with the Bloomberg logo.  
  `BloombergLogo(tower-b)`

**Conclusion**

- Tower B is located in New Haven.  
  `¬In(tower-b, newHaven)`

**Seqprover**

```
X@((in(X,newHaven) -> ~high(X))), X@((yaleHousing(X) -> in(X,newHaven))), X@((in(X,manhattan) -> high(X))), X@((bloomberg(X) -> in(X,manhattan))), X@((bloombergLogo(X) -> bloomberg(X))), yaleHousing('tower-a'), bloombergLogo('tower-b') --> ~in('tower-b',newHaven)
```

## ARG-54 — False (FOLIO train example 193, story 65)

**Premises**

- If a person coaches a football club, the person is a football coach.  
  `∀x ∀y ((Coach(x, y) ∧ FootballClub(y)) → FootballCoach(x))`
- If a person has a position in a club in a year, and the club is in NFL in the same year, the person plays in NFL.  
  `∀w ∀x ∀y ∀z ((PlayPositionFor(x, w, y, z) ∧ InNFL(y, z)) → PlayInNFL(x))`
- Minnesota Vikings is a football club.  
  `FootballClub(minnesotaVikings)`
- Dennis Green coached Minnesota Vikings.  
  `Coach(dennisGreen, minnesotaVikings)`
- Cris Carter had 13 touchdown receptions.  
  `ReceiveTD(crisCarter, num13)`
- Minnesota Vikings were in the National Football League in 1997.  
  `InNFL(minnesotaVikings, yr1997)`
- John Randle was Minnesota Vikings defensive tackle in 1997.  
  `PlayPositionFor(johnRandle, defensiveTackle, minnesotaVikings, yr1997)`

**Conclusion**

- John Randle didn't play in the National Football League.  
  `¬PlayInNFL(johnRandle)`

**Seqprover**

```
X@(Y@(((coach(X,Y) /\ footballClub(Y)) -> footballCoach(X)))), W@(X@(Y@(Z@(((playPositionFor(X,W,Y,Z) /\ inNFL(Y,Z)) -> playInNFL(X)))))), footballClub(minnesotaVikings), coach(dennisGreen,minnesotaVikings), receiveTD(crisCarter,num13), inNFL(minnesotaVikings,yr1997), playPositionFor(johnRandle,defensiveTackle,minnesotaVikings,yr1997) --> ~playInNFL(johnRandle)
```

## ARG-55 — False (FOLIO train example 196, story 66)

**Premises**

- If a city holds a Summer Olympics, and the city is a US city, then the Summer Olympics will be in the US.  
  `∀x ∀y ((SummerOlympicsIn(x,y) ∧ In(x, unitedStates)) → SummerOlympicsIn(x, unitedStates))`
- If a city is in a state in the US, the city is a US city.  
  `∀x ∀y ((In(x, y) ∧ In(y, unitedStates)) → In(x, unitedStates))`
- If a city is in a state, and a Summer Olympics is in this city, then the Summer Olympics is in this state.  
  `∀x ∀y ∀z ((In(x, z) ∧ State(z) ∧ SummerOlympicsIn(x,y)) → SummerOlympicsIn(z, y))`
- The 2028 Summer Olympics is scheduled to take place in Los Angeles.  
  `SummerOlympicsIn(losAngeles, yr2028)`
- Los Angeles is a city in California.  
  `In(losAngeles, california)`
- Atlanta is a US city.  
  `In(atlanta, unitedStates)`
- Atlanta is in Georgia.  
  `In(california, unitedStates)`
- California is a state in the United States.  
  `In(atlanta, georgia)`
- Boxing, modern pentathlon, and weightlifting will be removed from The 2028 Summer Olympics.  
  `¬InSummerOlympicsIn(boxing, yr2028) ∧ (¬InSummerOlympicsIn(modern_pentathlon, yr2028)) ∧ (¬InSummerOlympicsIn(weightlifting, yr2028))`
- Atlanta in the United States held the 1996 Summer Olympics.  
  `SummerOlympicsIn(atlanta, yr1996)`

**Conclusion**

- The 1996 Summer Olympics is not in Georgia.  
  `¬SummerOlympicsIn(georgia, yr1996)`

**Seqprover**

```
X@(Y@(((summerOlympicsIn(X,Y) /\ in(X,unitedStates)) -> summerOlympicsIn(X,unitedStates)))), X@(Y@(((in(X,Y) /\ in(Y,unitedStates)) -> in(X,unitedStates)))), X@(Y@(Z@(((in(X,Z) /\ (state(Z) /\ summerOlympicsIn(X,Y))) -> summerOlympicsIn(Z,Y))))), summerOlympicsIn(losAngeles,yr2028), in(losAngeles,california), in(atlanta,unitedStates), in(california,unitedStates), in(atlanta,georgia), (~inSummerOlympicsIn(boxing,yr2028) /\ (~inSummerOlympicsIn(modern_pentathlon,yr2028) /\ ~inSummerOlympicsIn(weightlifting,yr2028))), summerOlympicsIn(atlanta,yr1996) --> ~summerOlympicsIn(georgia,yr1996)
```

## ARG-56 — False (FOLIO train example 199, story 67)

**Premises**

- If an album is written by a rock band, then the genre of the album is rock.  
  `∀x ∀y ∀z (AlbumByBand(x, y) ∧ RockBand(y, z) → Genre(x, rock))`
- If a band writes an album winning an award, then this band wins this award.  
  `∀x ∀y ∀z (AlbumByBand(x, y) ∧ AlbumAward(x, z) → RockBandAward(y, z))`
- Trouble at the Henhouse is an album by The Tragically Hip.  
  `AlbumByBand(trouble_at_the_Henhouse, the_Tragically_Hip)`
- The Tragically Hip is a Canadian rock band.  
  `RockBand(the_Tragically_Hip, canada)`
- The song "Butts Wigglin'" is in Trouble at the Henhouse.  
  `SongInAlbum(butts_Wigglin, trouble_at_the_Henhouse)`
- Trouble at the Henhouse won the Album of the Year award.  
  `AlbumAward(trouble_at_the_Henhouse, the_Album_of_the_Year)`
- A song in Trouble at the Henhouse appeared in a film.  
  `∃x (SongInFilm(x) ∧ SongInAlbum(x, trouble_at_the_Henhouse))`

**Conclusion**

- No Canadian rock band has won the Album of the Year award.  
  `¬∃x(RockBand(x, canada) ∧ Award(x, theAlbumOfTheYear))`

**Seqprover**

```
X@(Y@(Z@(((albumByBand(X,Y) /\ rockBand(Y,Z)) -> genre(X,rock))))), X@(Y@(Z@(((albumByBand(X,Y) /\ albumAward(X,Z)) -> rockBandAward(Y,Z))))), albumByBand(trouble_at_the_Henhouse,the_Tragically_Hip), rockBand(the_Tragically_Hip,canada), songInAlbum(butts_Wigglin,trouble_at_the_Henhouse), albumAward(trouble_at_the_Henhouse,the_Album_of_the_Year), X#((songInFilm(X) /\ songInAlbum(X,trouble_at_the_Henhouse))) --> ~X#((rockBand(X,canada) /\ award(X,theAlbumOfTheYear)))
```

## ARG-57 — False (FOLIO train example 202, story 68)

**Premises**

- Lana Wilson directed After Tiller, The Departure, and Miss Americana.  
  `DirectedBy(afterTiller, lanaWilson) ∧ DirectedBy(theDeparture, lanaWilson) ∧ DirectedBy(missAmericana, lanaWilson)`
- If a film is directed by a person, the person is a filmmaker.  
  `∀x ∀y (DirectedBy(x, y) → Filmmaker(y))`
- After Tiller is a documentary.  
  `Documentary(afterTiller)`
- The documentary is a type of film.  
  `∀x (Documentary(x) → Film(x))`
- Lana Wilson is from Kirkland.  
  `From(lanaWilson, kirkland)`
- Kirkland is a US city.  
  `In(kirkland, unitedStates)`
- If a person is from a city in a country, the person is from the country.  
  `∀x ∀y ∀z ((From(x, y) ∧ In(y, z)) → From(x, z))`
- After Tiller is nominated for the Independent Spirit Award for Best Documentary.  
  `Nomination(afterTiller, theIndependentSpiritAwardForBestDocumentary)`

**Conclusion**

- Miss Americana is not directed by a filmmaker from Kirkland.  
  `¬∃x(Filmmaker(x) ∧ From(x, kirkland) ∧ DirectedBy(missAmericana, x))`

**Seqprover**

```
(directedBy(afterTiller,lanaWilson) /\ (directedBy(theDeparture,lanaWilson) /\ directedBy(missAmericana,lanaWilson))), X@(Y@((directedBy(X,Y) -> filmmaker(Y)))), documentary(afterTiller), X@((documentary(X) -> film(X))), from(lanaWilson,kirkland), in(kirkland,unitedStates), X@(Y@(Z@(((from(X,Y) /\ in(Y,Z)) -> from(X,Z))))), nomination(afterTiller,theIndependentSpiritAwardForBestDocumentary) --> ~X#((filmmaker(X) /\ (from(X,kirkland) /\ directedBy(missAmericana,X))))
```

## ARG-58 — False (FOLIO train example 205, story 69)

**Premises**

- Brian Winter is a Scottish football referee.  
  `Scottish(brianWinter) ∧ FootballReferee(brianWinter)`
- After being injured, Brian Winter retired in 2012.  
  `Retired(brianWinter) ∧ RetiredIn(brianWinter, yr2012)`
- Brian Winter was appointed as a referee observer after his retirement.  
  `RefereeObserver(brianWinter)`
- Some football referees become referee observers.  
  `∃x (FootballReferee(x) ∧ RefereeObserver(x))`
- The son of Brian Winter, Andy Winter, is a football player who plays for Hamilton Academical.  
  `SonOf(andyWinter, brianWinter) ∧ FootballPlayer(andyWinter) ∧ PlaysFor(andyWinter, hamiltonAcademical)`

**Conclusion**

- Brian Winter was not a referee observer.  
  `¬RefereeObserver(brianwinter)`

**Seqprover**

```
(scottish(brianWinter) /\ footballReferee(brianWinter)), (retired(brianWinter) /\ retiredIn(brianWinter,yr2012)), refereeObserver(brianWinter), X#((footballReferee(X) /\ refereeObserver(X))), (sonOf(andyWinter,brianWinter) /\ (footballPlayer(andyWinter) /\ playsFor(andyWinter,hamiltonAcademical))) --> ~refereeObserver(brianwinter)
```

## ARG-59 — False (FOLIO train example 239, story 78)

**Premises**

- Ableton has an office in Germany.  
  `OfficeIn(ableton, germany)`
- Ableton has an office in the USA.  
  `OfficeIn(ableton, unitedStates)`
- USA and Germany are different countries.  
  `¬SameCountry(germany, unitedStates)`
- Any company that has offices in different countries is a multinational company.  
  `∀x ∀y ∀z (OfficeIn(x, y) ∧ OfficeIn(x, z) ∧ (¬SameCountry(y, z)) → MultinationalCompany(x))`
- Ableton makes music software.  
  `MakesMusicSoftware(ableton)`

**Conclusion**

- Ableton does not have an office in Germany.  
  `¬OfficeIn(ableton, germany)`

**Seqprover**

```
officeIn(ableton,germany), officeIn(ableton,unitedStates), ~sameCountry(germany,unitedStates), X@(Y@(Z@(((officeIn(X,Y) /\ (officeIn(X,Z) /\ ~sameCountry(Y,Z))) -> multinationalCompany(X))))), makesMusicSoftware(ableton) --> ~officeIn(ableton,germany)
```

## ARG-60 — False (FOLIO train example 318, story 105)

**Premises**

- Show Your Love is a song recorded by the South Korean boy band BtoB 4u.  
  `Song(showYourLove) ∧ RecordedBy(showYourLove, bToB4u) ∧ SouthKorean(bToB4u) ∧ BoyBand(bToB4u)`
- The lead single of the extended play Inside is Show Your Love.  
  `ExtendedPlay(inside) ∧ LeadSingleOf(showYourLove, inside)`
- Show Your Love contains a hopeful message.  
  `Contains(showYourLove, hopefulMessage)`
- BtoB 4u member Hyunsik wrote Show Your Love.  
  `Member(hyunsik, btob4u) ∧ Wrote(hyunsik, showYourLove)`
- There is a music video for Show Your Love.  
  `Have(showYourLove, musicVideo)`

**Conclusion**

- Show Your Love wasn't written by a member of a boy band.  
  `∀x ∀y (Wrote(x, showYourLove) → ¬(BoyBand(y) ∧ MemberOf(x, y)))`

**Seqprover**

```
(song(showYourLove) /\ (recordedBy(showYourLove,bToB4u) /\ (southKorean(bToB4u) /\ boyBand(bToB4u)))), (extendedPlay(inside) /\ leadSingleOf(showYourLove,inside)), contains(showYourLove,hopefulMessage), (member(hyunsik,btob4u) /\ wrote(hyunsik,showYourLove)), have(showYourLove,musicVideo) --> X@(Y@((wrote(X,showYourLove) -> ~(boyBand(Y) /\ memberOf(X,Y)))))
```
