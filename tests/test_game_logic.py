import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from logic_utils import check_guess
from app import update_score

def test_score_does_not_go_negative_on_too_low():
    # Bug: score could go below 0 when subtracting 5 on a "Too Low" guess.
    # Starting at 0, a wrong guess should floor at 0, not produce -5.
    result = update_score(current_score=0, outcome="Too Low", attempt_number=1)
    assert result >= 0, f"Score went negative: {result}"

def test_score_does_not_go_negative_on_too_high():
    # Bug: score could go below 0 when subtracting 5 on an odd-attempt "Too High" guess.
    result = update_score(current_score=0, outcome="Too High", attempt_number=1)
    assert result >= 0, f"Score went negative: {result}"

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"
