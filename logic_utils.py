import random

def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None or raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    # FIX: Moved check_guess from app.py into logic_utils.py and corrected the high/low hint bug with AI collaboration
    try:
        guess_int = int(guess)
    except (TypeError, ValueError):
        guess_int = None

    try:
        secret_int = int(secret)
    except (TypeError, ValueError):
        secret_int = None

    if guess_int is not None and secret_int is not None:
        if guess_int == secret_int:
            return "Win", "🎉 Correct!"
        if guess_int > secret_int:
            return "Too High", "📉 Go LOWER!"
        return "Too Low", "📈 Go HIGHER!"

    if guess == secret:
        return "Win", "🎉 Correct!"
    if guess > secret:
        return "Too High", "📉 Go LOWER!"
    return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score


def reset_game_state(session_state, low: int, high: int, difficulty: str):
    # FIX: Extracted reset logic from app.py into logic_utils.py with AI-assisted refactor
    session_state.attempts = 1
    session_state.secret = random.randint(low, high)
    session_state.score = 0
    session_state.status = "playing"
    session_state.history = []
    session_state[f"guess_input_{difficulty}"] = ""
