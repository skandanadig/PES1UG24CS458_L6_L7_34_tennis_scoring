import pytest
from tennis_scoring import game_score, set_winner, match_status

# Initial starter test cases:
def test_game_start():
    assert game_score(0, 0) == "0-0"

def test_set_undecided():
    assert set_winner(3, 2) is None


# ==========================================
# Branch Coverage Tests for game_score:
# ==========================================

def test_game_score_negative_a():
    # Branch: a < 0 -> True
    with pytest.raises(ValueError, match="negative points"):
        game_score(-1, 0)

def test_game_score_negative_b():
    # Branch: a < 0 -> False, b < 0 -> True
    with pytest.raises(ValueError, match="negative points"):
        game_score(0, -1)

def test_game_score_deuce():
    # Branch: a >= 3 and b >= 3 -> True
    # Branch: a == b -> True ("deuce")
    assert game_score(3, 3) == "deuce"
    assert game_score(4, 4) == "deuce"

def test_game_score_deuce_game_a():
    # Branch: a >= 3 and b >= 3 -> True
    # Branch: a == b -> False
    # Branch: a - b >= 2 -> True ("game A")
    assert game_score(5, 3) == "game A"

def test_game_score_deuce_game_b():
    # Branch: a >= 3 and b >= 3 -> True
    # Branch: a == b -> False
    # Branch: a - b >= 2 -> False
    # Branch: b - a >= 2 -> True ("game B")
    assert game_score(3, 5) == "game B"

def test_game_score_advantage_a():
    # Branch: a >= 3 and b >= 3 -> True
    # Branch: a == b -> False
    # Branch: a - b >= 2 -> False
    # Branch: b - a >= 2 -> False
    # Branch: a > b -> True ("advantage A")
    assert game_score(4, 3) == "advantage A"

def test_game_score_advantage_b():
    # Branch: a >= 3 and b >= 3 -> True
    # Branch: a == b -> False
    # Branch: a - b >= 2 -> False
    # Branch: b - a >= 2 -> False
    # Branch: a > b -> False ("advantage B")
    assert game_score(3, 4) == "advantage B"

def test_game_score_four_points_win_a():
    # Branch: a >= 3 and b >= 3 -> False
    # Branch: a >= 4 -> True ("game A")
    assert game_score(4, 1) == "game A"

def test_game_score_four_points_win_b():
    # Branch: a >= 3 and b >= 3 -> False
    # Branch: a >= 4 -> False
    # Branch: b >= 4 -> True ("game B")
    assert game_score(1, 4) == "game B"

def test_game_score_standard_scores():
    # Branch: a >= 3 and b >= 3 -> False
    # Branch: a >= 4 -> False
    # Branch: b >= 4 -> False
    # Returns POINTS[a] + "-" + POINTS[b]
    assert game_score(1, 2) == "15-30"
    assert game_score(2, 1) == "30-15"
    assert game_score(3, 0) == "40-0"


# ==========================================
# Branch Coverage Tests for set_winner:
# ==========================================

def test_set_winner_a_win_regular():
    # Branch: a >= 6 and a - b >= 2 -> True ("A")
    assert set_winner(6, 4) == "A"
    assert set_winner(6, 0) == "A"

def test_set_winner_b_win_regular():
    # Branch: a >= 6 and a - b >= 2 -> False
    # Branch: b >= 6 and b - a >= 2 -> True ("B")
    assert set_winner(4, 6) == "B"
    assert set_winner(1, 6) == "B"

def test_set_winner_a_tiebreak_win():
    # Branch: a == 7 and b == 6 -> True ("A")
    assert set_winner(7, 6) == "A"

def test_set_winner_b_tiebreak_win():
    # Branch: b == 7 and a == 6 -> True ("B")
    assert set_winner(6, 7) == "B"

def test_set_winner_in_progress():
    # Branch: all if-statements False -> returns None
    assert set_winner(5, 5) is None
    assert set_winner(6, 5) is None
    assert set_winner(5, 6) is None


# ==========================================
# Branch Coverage Tests for match_status:
# ==========================================

def test_match_status_a_wins():
    # Branch: sets_a == needed -> True ("A wins")
    assert match_status(2, 0, 3) == "A wins"

def test_match_status_b_wins():
    # Branch: sets_a == needed -> False
    # Branch: sets_b == needed -> True ("B wins")
    assert match_status(1, 2, 3) == "B wins"

def test_match_status_decider():
    # Branch: sets_a == needed -> False
    # Branch: sets_b == needed -> False
    # Branch: sets_a == needed - 1 and sets_b == needed - 1 -> True ("decider")
    assert match_status(1, 1, 3) == "decider"
    assert match_status(2, 2, 5) == "decider"

def test_match_status_in_progress():
    # Branch: all if-statements False -> returns "in progress"
    assert match_status(1, 0, 5) == "in progress"
    assert match_status(0, 0, 3) == "in progress"
