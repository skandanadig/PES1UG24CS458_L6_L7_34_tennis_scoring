import pytest
from tennis_scoring import game_score, set_winner, match_status

# Initial starter test cases:
def test_game_start():
    assert game_score(0, 0) == "0-0"

def test_set_undecided():
    assert set_winner(3, 2) is None

# Tests for 100% statement / code coverage:
def test_game_score_negative():
    # Covers lines 5-6: if a < 0 or b < 0: raise ValueError
    with pytest.raises(ValueError, match="negative points"):
        game_score(-1, 0)
    with pytest.raises(ValueError, match="negative points"):
        game_score(0, -1)

def test_game_score_deuce():
    # Covers lines 8-9: if a == b: return "deuce"
    assert game_score(3, 3) == "deuce"

def test_game_score_deuce_game_a():
    # Covers lines 10-11: if a - b >= 2: return "game A"
    assert game_score(5, 3) == "game A"

def test_game_score_deuce_game_b():
    # Covers lines 12-13: if b - a >= 2: return "game B"
    assert game_score(3, 5) == "game B"

def test_game_score_advantage_a():
    # Covers lines 14-15: if a > b: return "advantage A"
    assert game_score(4, 3) == "advantage A"

def test_game_score_advantage_b():
    # Covers line 16: return "advantage B"
    assert game_score(3, 4) == "advantage B"

def test_game_score_win_a_pre_deuce():
    # Covers lines 17-18: if a >= 4: return "game A"
    assert game_score(4, 1) == "game A"

def test_game_score_win_b_pre_deuce():
    # Covers lines 19-20: if b >= 4: return "game B"
    assert game_score(1, 4) == "game B"

def test_game_score_standard_scores():
    # Covers line 21: return POINTS[a] + "-" + POINTS[b]
    assert game_score(1, 2) == "15-30"

def test_set_winner_a():
    # Covers lines 25-26: if a >= 6 and a - b >= 2: return "A"
    assert set_winner(6, 4) == "A"

def test_set_winner_b():
    # Covers lines 27-28: if b >= 6 and b - a >= 2: return "B"
    assert set_winner(4, 6) == "B"

def test_set_winner_a_tiebreak():
    # Covers lines 29-30: if a == 7 and b == 6: return "A"
    assert set_winner(7, 6) == "A"

def test_set_winner_b_tiebreak():
    # Covers lines 31-32: if b == 7 and a == 6: return "B"
    assert set_winner(6, 7) == "B"

def test_match_status_a_wins():
    # Covers lines 38-39: if sets_a == needed: return "A wins"
    assert match_status(2, 0, 3) == "A wins"

def test_match_status_b_wins():
    # Covers lines 40-41: if sets_b == needed: return "B wins"
    assert match_status(0, 2, 3) == "B wins"

def test_match_status_decider():
    # Covers lines 42-43: if sets_a == needed - 1 and sets_b == needed - 1: return "decider"
    assert match_status(1, 1, 3) == "decider"

def test_match_status_in_progress():
    # Covers line 44: return "in progress"
    assert match_status(1, 0, 5) == "in progress"
