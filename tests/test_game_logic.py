from logic_utils import check_guess, update_score

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


def test_update_score_too_high_always_subtracts():
    # Bug: "Too High" on even attempts was adding +5 instead of subtracting.
    # Both even and odd attempt numbers must subtract 5 from the score.
    score = 100
    assert update_score(score, "Too High", attempt_number=2) == 95  # even attempt
    assert update_score(score, "Too High", attempt_number=3) == 95  # odd attempt
