# Curated FOLIO argument base (60 arguments)

Source: folio_v2_validation.jsonl. Labels: True = conclusion follows; False = negation of the conclusion follows; Uncertain = neither follows.

| ID | FOLIO id | Story | Label | Premises |
|---|---|---|---|---|
| ARG-01 | 0 | 0 | True | 6 |
| ARG-02 | 243 | 80 | True | 5 |
| ARG-03 | 253 | 83 | True | 5 |
| ARG-04 | 388 | 131 | True | 5 |
| ARG-05 | 440 | 151 | True | 5 |
| ARG-06 | 560 | 197 | True | 6 |
| ARG-07 | 563 | 198 | True | 6 |
| ARG-08 | 578 | 203 | True | 5 |
| ARG-09 | 610 | 213 | True | 6 |
| ARG-10 | 657 | 232 | True | 6 |
| ARG-11 | 806 | 319 | True | 5 |
| ARG-12 | 808 | 319 | True | 5 |
| ARG-13 | 1033 | 386 | True | 6 |
| ARG-14 | 1269 | 441 | True | 5 |
| ARG-15 | 1273 | 442 | True | 5 |
| ARG-16 | 1314 | 456 | True | 5 |
| ARG-17 | 1412 | 483 | True | 6 |
| ARG-18 | 149 | 51 | True | 3 |
| ARG-19 | 171 | 58 | True | 4 |
| ARG-20 | 172 | 58 | True | 4 |
| ARG-21 | 1 | 0 | False | 6 |
| ARG-22 | 254 | 83 | False | 5 |
| ARG-23 | 304 | 101 | False | 5 |
| ARG-24 | 305 | 101 | False | 5 |
| ARG-25 | 306 | 101 | False | 5 |
| ARG-26 | 389 | 131 | False | 5 |
| ARG-27 | 441 | 151 | False | 5 |
| ARG-28 | 562 | 197 | False | 6 |
| ARG-29 | 580 | 203 | False | 5 |
| ARG-30 | 608 | 213 | False | 6 |
| ARG-31 | 805 | 319 | False | 5 |
| ARG-32 | 934 | 352 | False | 6 |
| ARG-33 | 1034 | 386 | False | 6 |
| ARG-34 | 1272 | 442 | False | 5 |
| ARG-35 | 1315 | 456 | False | 5 |
| ARG-36 | 1316 | 456 | False | 5 |
| ARG-37 | 148 | 51 | False | 3 |
| ARG-38 | 241 | 79 | False | 4 |
| ARG-39 | 291 | 96 | False | 4 |
| ARG-40 | 325 | 107 | False | 2 |
| ARG-41 | 2 | 0 | Uncertain | 6 |
| ARG-42 | 244 | 80 | Uncertain | 5 |
| ARG-43 | 245 | 80 | Uncertain | 5 |
| ARG-44 | 439 | 151 | Uncertain | 5 |
| ARG-45 | 564 | 198 | Uncertain | 6 |
| ARG-46 | 565 | 198 | Uncertain | 6 |
| ARG-47 | 579 | 203 | Uncertain | 5 |
| ARG-48 | 609 | 213 | Uncertain | 6 |
| ARG-49 | 658 | 232 | Uncertain | 6 |
| ARG-50 | 659 | 232 | Uncertain | 6 |
| ARG-51 | 802 | 318 | Uncertain | 6 |
| ARG-52 | 933 | 352 | Uncertain | 6 |
| ARG-53 | 1032 | 386 | Uncertain | 6 |
| ARG-54 | 1268 | 441 | Uncertain | 5 |
| ARG-55 | 1271 | 442 | Uncertain | 5 |
| ARG-56 | 1410 | 483 | Uncertain | 6 |
| ARG-57 | 1411 | 483 | Uncertain | 6 |
| ARG-58 | 147 | 51 | Uncertain | 3 |
| ARG-59 | 173 | 58 | Uncertain | 4 |
| ARG-60 | 242 | 79 | Uncertain | 4 |

## ARG-01 — True (FOLIO example 0, story 0)

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

## ARG-02 — True (FOLIO example 243, story 80)

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

## ARG-03 — True (FOLIO example 253, story 83)

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

## ARG-04 — True (FOLIO example 388, story 131)

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

## ARG-05 — True (FOLIO example 440, story 151)

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

## ARG-06 — True (FOLIO example 560, story 197)

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

## ARG-07 — True (FOLIO example 563, story 198)

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

## ARG-08 — True (FOLIO example 578, story 203)

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

## ARG-09 — True (FOLIO example 610, story 213)

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

## ARG-10 — True (FOLIO example 657, story 232)

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

## ARG-11 — True (FOLIO example 806, story 319)

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

## ARG-12 — True (FOLIO example 808, story 319)

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

## ARG-13 — True (FOLIO example 1033, story 386)

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

## ARG-14 — True (FOLIO example 1269, story 441)

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

## ARG-15 — True (FOLIO example 1273, story 442)

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

## ARG-16 — True (FOLIO example 1314, story 456)

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

## ARG-17 — True (FOLIO example 1412, story 483)

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

## ARG-18 — True (FOLIO example 149, story 51)

**Premises**

- The summer Olympic games is a sporting event.  
  `SportingEvent(olympics)`
- The last summer Olympic games was in Tokyo.  
  `LastSummerOlympics(tokyo)`
- The United States won the most medals in Tokyo.  
  `MostMedals(unitedStates, tokyo)`

**Conclusion**

- The United States won the most medals in the last summer Olympic games.  
  `∃x (LastSummerOlympics(x) ∧ MostMedals(unitedStates, x))`

**Seqprover**

```
sportingEvent(olympics), lastSummerOlympics(tokyo), mostMedals(unitedStates,tokyo) --> X#((lastSummerOlympics(X) /\ mostMedals(unitedStates,X)))
```

## ARG-19 — True (FOLIO example 171, story 58)

**Premises**

- Books contain tons of knowledge.  
  `∀x (Book(x) → Contains(x, knowledge))`
- When a person reads a book, that person gains knowledge.  
  `∀x ∀y (ReadBook(x, y) → Gains(x, knowledge))`
- If a person gains knowledge, they become smarter.  
  `∀x (Gains(x, knowledge) → Smarter(x))`
- Harry read the book “Walden” by Henry Thoreau.  
  `ReadBook(harry, walden) ∧ Book(walden)`

**Conclusion**

- Walden contains knowledge.  
  `Gains(harry, knowledge)`

**Seqprover**

```
X@((book(X) -> contains(X,knowledge))), X@(Y@((readBook(X,Y) -> gains(X,knowledge)))), X@((gains(X,knowledge) -> smarter(X))), (readBook(harry,walden) /\ book(walden)) --> gains(harry,knowledge)
```

## ARG-20 — True (FOLIO example 172, story 58)

**Premises**

- Books contain tons of knowledge.  
  `∀x (Book(x) → Contains(x, knowledge))`
- When a person reads a book, that person gains knowledge.  
  `∀x ∀y (ReadBook(x, y) → Gains(x, knowledge))`
- If a person gains knowledge, they become smarter.  
  `∀x (Gains(x, knowledge) → Smarter(x))`
- Harry read the book “Walden” by Henry Thoreau.  
  `ReadBook(harry, walden) ∧ Book(walden)`

**Conclusion**

- Harry is smarter than before.  
  `Smarter(harry)`

**Seqprover**

```
X@((book(X) -> contains(X,knowledge))), X@(Y@((readBook(X,Y) -> gains(X,knowledge)))), X@((gains(X,knowledge) -> smarter(X))), (readBook(harry,walden) /\ book(walden)) --> smarter(harry)
```

## ARG-21 — False (FOLIO example 1, story 0)

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

## ARG-22 — False (FOLIO example 254, story 83)

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

## ARG-23 — False (FOLIO example 304, story 101)

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

## ARG-24 — False (FOLIO example 305, story 101)

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

## ARG-25 — False (FOLIO example 306, story 101)

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

## ARG-26 — False (FOLIO example 389, story 131)

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

## ARG-27 — False (FOLIO example 441, story 151)

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

## ARG-28 — False (FOLIO example 562, story 197)

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

## ARG-29 — False (FOLIO example 580, story 203)

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

## ARG-30 — False (FOLIO example 608, story 213)

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

## ARG-31 — False (FOLIO example 805, story 319)

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

## ARG-32 — False (FOLIO example 934, story 352)

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

## ARG-33 — False (FOLIO example 1034, story 386)

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

## ARG-34 — False (FOLIO example 1272, story 442)

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

## ARG-35 — False (FOLIO example 1315, story 456)

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

## ARG-36 — False (FOLIO example 1316, story 456)

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

## ARG-37 — False (FOLIO example 148, story 51)

**Premises**

- The summer Olympic games is a sporting event.  
  `SportingEvent(olympics)`
- The last summer Olympic games was in Tokyo.  
  `LastSummerOlympics(tokyo)`
- The United States won the most medals in Tokyo.  
  `MostMedals(unitedStates, tokyo)`

**Conclusion**

- The last summer Olympic games were not in Tokyo.  
  `¬LastSummerOlympics(tokyo)`

**Seqprover**

```
sportingEvent(olympics), lastSummerOlympics(tokyo), mostMedals(unitedStates,tokyo) --> ~lastSummerOlympics(tokyo)
```

## ARG-38 — False (FOLIO example 241, story 79)

**Premises**

- Robert Lewandowski is a striker.  
  `Striker(robertLewandowski)`
- Strikers are soccer players.  
  `∀x (Striker(x) → SoccerPlayer(x))`
- Robert Lewandowski left Bayern Munchen.  
  `Left(robertLewandowski, bayernMunchen)`
- If a player leaves a team they no longer play for that team.  
  `∀x ∀y (Left(x, y) → ¬PlaysFor(x, y))`

**Conclusion**

- Robert Lewandowski plays for Bayern Munchen.  
  `PlaysFor(robertLewandowski, bayernMunchen)`

**Seqprover**

```
striker(robertLewandowski), X@((striker(X) -> soccerPlayer(X))), left(robertLewandowski,bayernMunchen), X@(Y@((left(X,Y) -> ~playsFor(X,Y)))) --> playsFor(robertLewandowski,bayernMunchen)
```

## ARG-39 — False (FOLIO example 291, story 96)

**Premises**

- Diamond Mine is a professional wrestling stable formed in WWE.  
  `ProfessionalWrestlingStable(diamondMine) ∧ In(diamondMine, wWE)`
- Roderick Strong leads Diamond Mine.  
  `Leads(roderickStrong, diamondMine)`
- Diamond Mine includes the Creed Brothers and Ivy Nile.  
  `Includes(diamondMine, creedBrothers) ∧ Includes(diamondMine, ivyNile)`
- Imperium has a feud with Diamond Mine.  
  `Feuds(imperium, diamondMine)`

**Conclusion**

- Imperium doesn't have a feud with a professional wrestling stable that includes Ivy Nile.  
  `∀x ((ProfessionalWrestlingStable(x) ∧ Includes(x, ivynile)) → ¬Feuds(imperium, x))`

**Seqprover**

```
(professionalWrestlingStable(diamondMine) /\ in(diamondMine,wWE)), leads(roderickStrong,diamondMine), (includes(diamondMine,creedBrothers) /\ includes(diamondMine,ivyNile)), feuds(imperium,diamondMine) --> X@(((professionalWrestlingStable(X) /\ includes(X,ivynile)) -> ~feuds(imperium,X)))
```

## ARG-40 — False (FOLIO example 325, story 107)

**Premises**

- Heinrich Schmidt was a German politician.  
  `German(heinrichSchmidt) ∧ Politician(heinrichSchmidt)`
- Heinrich Schmidt was also a member of the Prussian State Parliament and the Nazi Reichstag.  
  `Member(heinrichSchmidt, prussianStateParliament) ∧ Member(heinrichSchmidt, naziReichstag)`

**Conclusion**

- No politicians are part of the Nazi Reichstag.  
  `∀x (Politician(x) → ¬Member(x, naziReichstag))`

**Seqprover**

```
(german(heinrichSchmidt) /\ politician(heinrichSchmidt)), (member(heinrichSchmidt,prussianStateParliament) /\ member(heinrichSchmidt,naziReichstag)) --> X@((politician(X) -> ~member(X,naziReichstag)))
```

## ARG-41 — Uncertain (FOLIO example 2, story 0)

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

- Joey is a wild turkey.  
  `WildTurkey(joey)`

**Seqprover**

```
X@((wildTurkey(X) -> (easternWildTurkey(X) \/ (osceolaWildTurkey(X) \/ (gouldsWildTurkey(X) \/ (merriamsWildTurkey(X) \/ (riograndeWildTurkey(X) \/ ocellatedWildTurkey(X)))))))), ~easternWildTurkey(tom), ~osceolaWildTurkey(tom), ~gouldsWildTurkey(tom), ~(merriamsWildTurkey(tom) \/ riograndeWildTurkey(tom)), wildTurkey(tom) --> wildTurkey(joey)
```

## ARG-42 — Uncertain (FOLIO example 244, story 80)

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

- Harry Potter was published by New Vessel Press.  
  `PublishedBy(harryPotter, newVesselPress)`

**Seqprover**

```
(publishingHouse(newVesselPress) /\ specializesInTranslatingIntoEnglish(newVesselPress,foreignLiterature)), X@(((book(X) /\ publishedBy(X,newVesselPress)) -> in(X,english))), (book(neapolitanChronicles) /\ publishedBy(neapolitanChronicles,newVesselPress)), translatedFrom(neapolitanChronicles,italian), (book(palaceOfFlies) /\ publishedBy(palaceOfFlies,newVesselPress)) --> publishedBy(harryPotter,newVesselPress)
```

## ARG-43 — Uncertain (FOLIO example 245, story 80)

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

- Palace of Flies was translated from Italian.  
  `TranslatedFrom(palaceOfFlies, italian)`

**Seqprover**

```
(publishingHouse(newVesselPress) /\ specializesInTranslatingIntoEnglish(newVesselPress,foreignLiterature)), X@(((book(X) /\ publishedBy(X,newVesselPress)) -> in(X,english))), (book(neapolitanChronicles) /\ publishedBy(neapolitanChronicles,newVesselPress)), translatedFrom(neapolitanChronicles,italian), (book(palaceOfFlies) /\ publishedBy(palaceOfFlies,newVesselPress)) --> translatedFrom(palaceOfFlies,italian)
```

## ARG-44 — Uncertain (FOLIO example 439, story 151)

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

- Barutin Cove is named after all islands in Antarctica.  
  `∀x (LocatedIn(x, antarctica) → NamedAfter(barutinCove, x))`

**Seqprover**

```
(cove(barutinCove) /\ (namedAfter(barutinCove,barutinSettlement) /\ locatedIn(barutinSettlement,bulgaria))), locatedIn(barutinCove,snowIsland), (locatedIn(snowIsland,southShetlandIslands) /\ (locatedIn(greenwichIsland,southShetlandIslands) /\ locatedIn(deceptionIsland,southShetlandIslands))), locatedIn(southShetlandIslands,antarctica), X@(Y@(Z@(((locatedIn(X,Y) /\ locatedIn(Y,Z)) -> locatedIn(X,Z))))) --> X@((locatedIn(X,antarctica) -> namedAfter(barutinCove,X)))
```

## ARG-45 — Uncertain (FOLIO example 564, story 198)

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

- No one gets the flu.  
  `∀x (Human(x) → ¬Get(x, flu))`

**Seqprover**

```
X#((occurIn(monkeypoxVirus,X) /\ get(X,monkeypoxVirus))), X#((animal(X) /\ occurIn(monkeypoxVirus,X))), X@((human(X) -> mammal(X))), X@((mammal(X) -> animal(X))), X#((symptonOf(X,monkeypoxVirus) /\ (fever(X) \/ (headache(X) \/ (musclePain(X) \/ tired(X)))))), X@(((human(X) /\ get(X,flu)) -> feel(X,tired))) --> X@((human(X) -> ~get(X,flu)))
```

## ARG-46 — Uncertain (FOLIO example 565, story 198)

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

- Symptoms of Monkeypox include coughing.  
  `∃x (SymptonOf(x, monkeypoxVirus) ∧ Coughing(x))`

**Seqprover**

```
X#((occurIn(monkeypoxVirus,X) /\ get(X,monkeypoxVirus))), X#((animal(X) /\ occurIn(monkeypoxVirus,X))), X@((human(X) -> mammal(X))), X@((mammal(X) -> animal(X))), X#((symptonOf(X,monkeypoxVirus) /\ (fever(X) \/ (headache(X) \/ (musclePain(X) \/ tired(X)))))), X@(((human(X) /\ get(X,flu)) -> feel(X,tired))) --> X#((symptonOf(X,monkeypoxVirus) /\ coughing(X)))
```

## ARG-47 — Uncertain (FOLIO example 579, story 203)

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

- Space is a vampire.  
  `Vampire(space)`

**Seqprover**

```
X@((plunger(X) -> suck(X))), X@((vacuum(X) -> suck(X))), X@((vampire(X) -> suck(X))), vacuum(space), (householdAppliance(duster) /\ ~suck(duster)) --> vampire(space)
```

## ARG-48 — Uncertain (FOLIO example 609, story 213)

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

- German is a Romance language.  
  `RomanceLanguage(german)`

**Seqprover**

```
X@((romanceLanguage(X) -> indoEuropeanLanguage(X))), X@((romanceLanguage(X) -> memberOf(X,languageFamily))), X@(Y@(Z@(((memberOf(X,Z) /\ memberOf(Y,Z)) -> (related(X,Y) /\ related(Y,X)))))), (romanceLanguage(french) /\ romanceLanguage(spanish)), related(german,spanish), X@((language(X) -> ~related(basque,X))) --> romanceLanguage(german)
```

## ARG-49 — Uncertain (FOLIO example 658, story 232)

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

- Beijing is located in southern China.  
  `LocatedIn(beijing, southernChina)`

**Seqprover**

```
capitalOf(beijing,peoplesRepublicOfChina), X#((capitalOf(beijing,X) -> worldsMostPopulousNation(X))), locatedIn(beijing,northernChina), (hosted(beijing,'2008SummerOlympics') /\ hosted(beijing,'2008SummerParalympicGames')), (hosted(beijing,summerOlympics) /\ (hosted(beijing,winterOlympics) /\ (hosted(beijing,summerParalympicGames) /\ hosted(beijing,winterParalympicGames)))), X#((university(X) /\ (inBeijing(X) /\ consistentlyRankAmongTheBestIn(X,theWorld)))) --> locatedIn(beijing,southernChina)
```

## ARG-50 — Uncertain (FOLIO example 659, story 232)

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

- Beijing is the second largest Chinese city.  
  `SecondLargestChineseCity(beijing)`

**Seqprover**

```
capitalOf(beijing,peoplesRepublicOfChina), X#((capitalOf(beijing,X) -> worldsMostPopulousNation(X))), locatedIn(beijing,northernChina), (hosted(beijing,'2008SummerOlympics') /\ hosted(beijing,'2008SummerParalympicGames')), (hosted(beijing,summerOlympics) /\ (hosted(beijing,winterOlympics) /\ (hosted(beijing,summerParalympicGames) /\ hosted(beijing,winterParalympicGames)))), X#((university(X) /\ (inBeijing(X) /\ consistentlyRankAmongTheBestIn(X,theWorld)))) --> secondLargestChineseCity(beijing)
```

## ARG-51 — Uncertain (FOLIO example 802, story 318)

**Premises**

- Some show airing at 8 pm on Monday gives out roses on TV.  
  `∃x (Show(x) ∧ AiringAtOn(x, 8PMMonday) ∧ GivenOutOn(x, rose, tV))`
- If a show gives out roses on TV, then the show is an episode of The Bachelor.  
  `∀x (Show(x) ∧ GivenOutOnAt(rose, tV, x) → TheBachelor(x))`
- The Bachelor portrays the lives of real people.  
  `∀x (TheBachelor(x) → Portray(x, lifeOfRealPeople))`
- All shows portraying the lives of real people are reality TV shows.  
  `∀x (Portray(x, liveOfRealPeople) → RealityTVShow(x))`
- Breaking Bad is a show.  
  `Show(breakingBad)`
- Breaking Bad is not a reality TV show.  
  `¬RealityTVShow(breakingBad)`

**Conclusion**

- Breaking Bad is on Monday at 8 pm.  
  `∀x (MondayAt8PM(x) ∧ On(breakingBad, x))`

**Seqprover**

```
X#((show(X) /\ (airingAtOn(X,'8PMMonday') /\ givenOutOn(X,rose,tV)))), X@(((show(X) /\ givenOutOnAt(rose,tV,X)) -> theBachelor(X))), X@((theBachelor(X) -> portray(X,lifeOfRealPeople))), X@((portray(X,liveOfRealPeople) -> realityTVShow(X))), show(breakingBad), ~realityTVShow(breakingBad) --> X@((mondayAt8PM(X) /\ on(breakingBad,X)))
```

## ARG-52 — Uncertain (FOLIO example 933, story 352)

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

- The Harvard Weekly Book club has legal obligations.  
  `LegalObligation(harvardWeeklyBookClub)`

**Seqprover**

```
X@((businessOrganization(X) -> legalEntity(X))), X@((company(X) -> businessOrganization(X))), X@((privateCompany(X) -> company(X))), X@((legalEntity(X) -> createdUnderLaw(X))), X@((legalEntity(X) -> legalObligation(X))), (createdUnderLaw(harvardWeeklyBookClub) -> ~privateCompany(harvardWeeklyBookClub)) --> legalObligation(harvardWeeklyBookClub)
```

## ARG-53 — Uncertain (FOLIO example 1032, story 386)

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

- Colorectal cancer is a kind of severe cancer  
  `SevereCancer(colorectalCancer)`

**Seqprover**

```
X@((deadlyDiseases(X) -> comeWith(X,lowSurvivalRate))), X@((severeCancer(X) -> deadlyDiseases(X))), X@((bileDuctCancer(X) -> severeCancer(X))), X@((cholangiocarcinoma(X) -> bileDuctCancer(X))), X@((mildFlu(X) -> ~comeWith(X,lowSurvivalRate))), ~(bileDuctCancer(colorectalCancer) /\ comeWith(colorectalCancer,lowSurvivalRate)) --> severeCancer(colorectalCancer)
```

## ARG-54 — Uncertain (FOLIO example 1268, story 441)

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

- Tom is a grumpy person.  
  `Grumpy(tom)`

**Seqprover**

```
X@((niceTo(X,animal) -> ~meanTo(X,animal))), X#((grumpy(X) /\ meanTo(X,animal))), X@((animalLover(X) -> niceTo(X,animal))), X@((petOwner(X) -> animalLover(X))), petOwner(tom) --> grumpy(tom)
```

## ARG-55 — Uncertain (FOLIO example 1271, story 442)

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

- Ted is a pet.  
  `Pet(ted)`

**Seqprover**

```
X@((brownSwissCattle(X) -> cow(X))), X#((pet(X) /\ brownSwissCattle(X))), X@((cow(X) -> domesticatedAnimal(X))), X@((aligator(X) -> ~domesticatedAnimal(X))), aligator(ted) --> pet(ted)
```

## ARG-56 — Uncertain (FOLIO example 1410, story 483)

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

- Vladimir is a Russian federation official  
  `Russian(vladimir) ∧ FederationOfficial(vladimir)`

**Seqprover**

```
X@((canRegisterToVoteIn(X,unitedStates) -> canParticipateIn(X,'2024UnitedStatesElection'))), X@((have(X,unitedStatesCitizenship) -> canRegisterToVoteIn(X,unitedStates))), X@((have(X,unitedStatesCitizenship) \/ have(X,taiwaneseCitizenship))), X@(((russian(X) /\ federationOfficial(X)) -> ~have(X,taiwaneseCitizenship))), (~have(vladimir,taiwaneseCitizenship) /\ ~managerAt(vladimir,gazprom)), ((russian(ekaterina) /\ federationOfficial(ekaterina)) \/ canRegisterToVoteIn(ekaterina,unitedStates)) --> (russian(vladimir) /\ federationOfficial(vladimir))
```

## ARG-57 — Uncertain (FOLIO example 1411, story 483)

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

- Vladimir is not a Russian federation official  
  `¬(Russian(vladimir) ∧ FederationOfficial(vladimir))`

**Seqprover**

```
X@((canRegisterToVoteIn(X,unitedStates) -> canParticipateIn(X,'2024UnitedStatesElection'))), X@((have(X,unitedStatesCitizenship) -> canRegisterToVoteIn(X,unitedStates))), X@((have(X,unitedStatesCitizenship) \/ have(X,taiwaneseCitizenship))), X@(((russian(X) /\ federationOfficial(X)) -> ~have(X,taiwaneseCitizenship))), (~have(vladimir,taiwaneseCitizenship) /\ ~managerAt(vladimir,gazprom)), ((russian(ekaterina) /\ federationOfficial(ekaterina)) \/ canRegisterToVoteIn(ekaterina,unitedStates)) --> ~(russian(vladimir) /\ federationOfficial(vladimir))
```

## ARG-58 — Uncertain (FOLIO example 147, story 51)

**Premises**

- The summer Olympic games is a sporting event.  
  `SportingEvent(olympics)`
- The last summer Olympic games was in Tokyo.  
  `LastSummerOlympics(tokyo)`
- The United States won the most medals in Tokyo.  
  `MostMedals(unitedStates, tokyo)`

**Conclusion**

- The world championships is a sporting event.  
  `SportingEvent(champs)`

**Seqprover**

```
sportingEvent(olympics), lastSummerOlympics(tokyo), mostMedals(unitedStates,tokyo) --> sportingEvent(champs)
```

## ARG-59 — Uncertain (FOLIO example 173, story 58)

**Premises**

- Books contain tons of knowledge.  
  `∀x (Book(x) → Contains(x, knowledge))`
- When a person reads a book, that person gains knowledge.  
  `∀x ∀y (ReadBook(x, y) → Gains(x, knowledge))`
- If a person gains knowledge, they become smarter.  
  `∀x (Gains(x, knowledge) → Smarter(x))`
- Harry read the book “Walden” by Henry Thoreau.  
  `ReadBook(harry, walden) ∧ Book(walden)`

**Conclusion**

- A smarter person has gained knowledge.  
  `∀x (Smarter(x) → GainKnowledge(x))`

**Seqprover**

```
X@((book(X) -> contains(X,knowledge))), X@(Y@((readBook(X,Y) -> gains(X,knowledge)))), X@((gains(X,knowledge) -> smarter(X))), (readBook(harry,walden) /\ book(walden)) --> X@((smarter(X) -> gainKnowledge(X)))
```

## ARG-60 — Uncertain (FOLIO example 242, story 79)

**Premises**

- Robert Lewandowski is a striker.  
  `Striker(robertLewandowski)`
- Strikers are soccer players.  
  `∀x (Striker(x) → SoccerPlayer(x))`
- Robert Lewandowski left Bayern Munchen.  
  `Left(robertLewandowski, bayernMunchen)`
- If a player leaves a team they no longer play for that team.  
  `∀x ∀y (Left(x, y) → ¬PlaysFor(x, y))`

**Conclusion**

- Robert Lewandowski is a star.  
  `SoccerStar(robertLewandowski)`

**Seqprover**

```
striker(robertLewandowski), X@((striker(X) -> soccerPlayer(X))), left(robertLewandowski,bayernMunchen), X@(Y@((left(X,Y) -> ~playsFor(X,Y)))) --> soccerStar(robertLewandowski)
```
