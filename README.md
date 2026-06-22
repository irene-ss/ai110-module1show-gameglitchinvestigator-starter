# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose: This is a guessing game with 3 modes, that allows users to guess a certain number of times. Each guess will yield clues to lead you to the number while also tracking guess history and points.
- [ ] Detail which bugs you found : I mainly found three bugs: 1. the hint was wrong 2. The reset button did not work as expected. 3. Guess history was not being properly tracked.
- [ ] Explain what fixes you applied : The bugs I fixed were the rest button that now renews attempts left and the hint message that now correctly displays the message.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. User enters a guess of 30
2. Game returns "Too High"
3. User enters a guess of 17 → "Too High"
4. User enters a guess of 12. -> correct, user wins
5. Score updates correctly after each guess
6. User guesses correctly so game ends.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# No output, however the precense of no error messages means the tests passed.
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
