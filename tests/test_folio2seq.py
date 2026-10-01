"""Tests for the FOLIO  ->  Seqprover converter."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import pytest

from folio2seq import (
    Candidate,
    ConvertError,
    fol_to_seqprover,
    parse_fol,
    select,
    seqprover_term,
    sequent_for,
)


def s(fol: str) -> str:
    return fol_to_seqprover(fol)


# ---- tokens and atoms --------------------------------------------------------

def test_predicate_is_lowercased_and_variable_uppercased():
    assert s("∀x Student(x)") == "X@(student(X))"


def test_constant_stays_lowercase():
    assert s("Favorite(mia, schoolTalentShow)") == "favorite(mia,schoolTalentShow)"


def test_numeric_constant_kept_as_integer():
    assert s("BornIn(john, 1984)") == "bornIn(john,1984)"


def test_digit_initial_alphanumeric_constant_is_quoted():
    assert s("Won(trump, 2024UnitedStatesElection)") == "won(trump,'2024UnitedStatesElection')"


def test_constant_that_clashes_with_variable_name_is_quoted():
    # 'X' in FOLIO would be an uppercase constant; must not become a Prolog variable.
    assert s("P(Ab)") == "p('Ab')"


def test_non_ascii_constant_is_quoted():
    assert s("LostTo(k, świątek)") == "lostTo(k,'świątek')"


def test_hyphenated_constant_is_quoted():
    assert s("GrewUpIn(k, health-consciousChildhoodHome)") == "grewUpIn(k,'health-consciousChildhoodHome')"


def test_double_negation_is_spaced():
    assert s("¬¬A") == "~ ~a"


def test_implication_of_negation_does_not_glue_operators():
    assert s("A → ¬B") == "(a -> ~b)"


def test_nullary_predicate_is_plain_atom():
    assert s("Raining") == "raining"


# ---- connectives and precedence ---------------------------------------------

def test_negation():
    assert s("¬Student(k)") == "~student(k)"


def test_conjunction_over_disjunction_is_parenthesised():
    # FOLIO precedence: ∧ binds tighter than ∨. Seqprover gives them equal
    # precedence and right associativity, so parentheses are required.
    assert s("A(k) ∧ B(k) ∨ C(k)") == "((a(k) /\\ b(k)) \\/ c(k))"


def test_disjunction_then_conjunction():
    assert s("A(k) ∨ B(k) ∧ C(k)") == "(a(k) \\/ (b(k) /\\ c(k)))"


def test_implication_is_lowest_precedence():
    assert s("A(k) ∧ B(k) → C(k) ∨ D(k)") == "((a(k) /\\ b(k)) -> (c(k) \\/ d(k)))"


def test_implication_is_right_associative():
    assert s("A → B → C") == "(a -> (b -> c))"


def test_negation_binds_tighter_than_conjunction():
    assert s("¬A ∧ B") == "(~a /\\ b)"


def test_negated_group():
    assert s("¬(A ∧ B)") == "~(a /\\ b)"


def test_chained_conjunction_flattens_right():
    assert s("A ∧ B ∧ C") == "(a /\\ (b /\\ c))"


# ---- quantifiers ------------------------------------------------------------

def test_universal_quantifier():
    assert s("∀x (Student(x) → Smart(x))") == "X@((student(X) -> smart(X)))"


def test_existential_quantifier():
    assert s("∃x (Student(x) ∧ Smart(x))") == "X#((student(X) /\\ smart(X)))"


def test_nested_quantifiers_without_space():
    assert s("∀x∃y Likes(x, y)") == "X@(Y#(likes(X,Y)))"


def test_quantifier_scope_is_the_following_unit_only():
    # ∀x P(x) ∧ Q(x) — quantifier scopes over P(x) only, matching FOL convention.
    # Q(x) then has a free x, which must be reported.
    with pytest.raises(ConvertError):
        s("∀x P(x) ∧ Q(x)")


def test_negated_quantifier():
    assert s("¬∃z In(a, z)") == "~Z#(in(a,Z))"


def test_variable_with_digit_suffix():
    assert s("∀x1 P(x1)") == "X1@(p(X1))"


# ---- rejection of unsupported input -----------------------------------------

@pytest.mark.parametrize("fol", ["A ⊕ B", "A ↔ B", "A ⟷ B", "¬(x = y)"])
def test_unsupported_connectives_are_rejected(fol):
    with pytest.raises(ConvertError):
        s(fol)


def test_free_variable_is_rejected():
    with pytest.raises(ConvertError):
        s("∀x (Student(x) ∧ OfferedBy(y, university) → WorkIn(x, library))")


def test_unbalanced_parentheses_rejected():
    with pytest.raises(ConvertError):
        s("∀x (Student(x)")


# ---- sequents ---------------------------------------------------------------

def test_sequent_for_true_label():
    seq = sequent_for(["∀x (A(x) → B(x))", "A(c)"], "B(c)", "True")
    assert seq == {
        "goal": "X@((a(X) -> b(X))), a(c) --> b(c)",
        "negated_goal": "X@((a(X) -> b(X))), a(c) --> ~b(c)",
        "expected": {"goal": True, "negated_goal": False},
    }


def test_sequent_for_false_label_expects_negation_provable():
    seq = sequent_for(["¬A(c)"], "A(c)", "False")
    assert seq["expected"] == {"goal": False, "negated_goal": True}


def test_negated_goal_of_negative_conclusion_does_not_glue_tildes():
    seq = sequent_for(["A(c)"], "¬B(c)", "Uncertain")
    assert seq["negated_goal"] == "a(c) --> ~ ~b(c)"


def test_sequent_for_uncertain_label_expects_neither():
    seq = sequent_for(["A(c)"], "B(c)", "Uncertain")
    assert seq["expected"] == {"goal": False, "negated_goal": False}


def test_seqprover_term_wraps_in_batch_syntax():
    term = seqprover_term("a --> b", output="pretty")
    assert term == "pretty.\na --> b.\n"


# ---- round trip on a real FOLIO example -------------------------------------

def test_real_folio_formula():
    fol = ("∀x (InThisClub(x) ∧ PerformOftenIn(x, schoolTalentShow) → "
           "Attend(x, schoolEvent) ∧ VeryEngagedWith(x, schoolEvent))")
    out = s(fol)
    assert out == ("X@(((inThisClub(X) /\\ performOftenIn(X,schoolTalentShow)) -> "
                   "(attend(X,schoolEvent) /\\ veryEngagedWith(X,schoolEvent))))")
    # the tree is well formed
    assert parse_fol(fol) is not None


# ---- selection -------------------------------------------------------------

def _cand(eid, story, label, n, split="validation"):
    return Candidate(example_id=eid, story_id=story, label=label, premises=["p"] * n,
                     premises_fol=["P"] * n, conclusion="c", conclusion_fol="C", split=split)


def test_select_filters_labels_and_prefers_long_arguments():
    cands = [_cand(1, 1, "True", 5), _cand(2, 2, "True", 3), _cand(3, 3, "Uncertain", 6),
             _cand(4, 4, "False", 5), _cand(5, 5, "True", 6)]
    out = select(cands, per_label=2, min_premises=5, max_per_story=3, labels=("True", "False"))
    assert [c.example_id for c in out] == [1, 5, 4]


def test_select_orders_by_split_priority_then_id():
    cands = [_cand(1, 1, "True", 5, split="train"), _cand(9, 9, "True", 5, split="validation")]
    out = select(cands, per_label=2, min_premises=5, max_per_story=3, labels=("True",),
                 split_order=("validation", "train"))
    assert [c.example_id for c in out] == [9, 1]


def test_select_caps_per_story_within_split():
    cands = [_cand(i, 7, "True", 5) for i in range(1, 6)]
    out = select(cands, per_label=5, min_premises=5, max_per_story=3, labels=("True",))
    assert len(out) == 3
