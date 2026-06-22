from types import SimpleNamespace
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from logic_utils import check_guess, parse_guess, reset_game_state


def test_winning_guess():
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert message == "🎉 Correct!"


def test_parse_guess_rejects_negative_numbers():
    ok, value, err = parse_guess("-5", low=1, high=100)
    assert ok is False
    assert value is None
    assert err == "Enter a whole number between 1 and 100."


def test_parse_guess_rejects_decimal_inputs():
    ok, value, err = parse_guess("42.5", low=1, high=100)
    assert ok is False
    assert value is None
    assert err == "Enter a whole number between 1 and 100."


def test_parse_guess_rejects_extremely_large_values():
    ok, value, err = parse_guess("999999999999999999999999999999999", low=1, high=100)
    assert ok is False
    assert value is None
    assert err == "Enter a whole number between 1 and 100."

def test_guess_too_high():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert message == "📉 Go LOWER!"

def test_guess_too_low():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!"

def test_guess_with_string_secret_handles_logic_correctly():
    outcome, message = check_guess(50, "50")
    assert outcome == "Win"
    assert message == "🎉 Correct!"


def test_reset_game_state_resets_all_values():
    # FIX: Regression test added for the new reset behavior after AI-assisted bug fixes
    state = SimpleNamespace(
        attempts=4,
        secret=999,
        score=42,
        status="lost",
        history=[5, 15, 25],
        guess_input_Easy="123"
    )

    reset_game_state(state, low=1, high=20, difficulty="Easy")

    assert state.attempts == 1
    assert 1 <= state.secret <= 20
    assert state.secret != 999
    assert state.score == 0
    assert state.status == "playing"
    assert state.history == []
    assert state.guess_input_Easy == ""
