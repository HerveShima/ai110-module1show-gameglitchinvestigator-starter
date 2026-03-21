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

- [x] **Game purpose:** A number guessing game where the player tries to guess a secret number within a limited number of attempts. Feedback hints guide the player higher or lower, and a score tracks performance across attempts.

- [x] **Bugs found:**
  - Hard difficulty range (`1–50`) was easier than Normal (`1–100`)
  - Hint messages were swapped — "Go HIGHER" showed when the guess was too high
  - `show_hint` checkbox defaulted to `True`, always showing hints
  - Secret was randomly cast to a string on even attempts, breaking comparisons
  - `attempts` session state initialized at `1` instead of `0`
  - New game never reset `status`, so a won/lost game blocked further play
  - Score started at `0`, going negative after just a few wrong guesses
  - `update_score` added `+5` points on even-attempt "Too High" guesses instead of subtracting
  - Info banner hardcoded "1 and 100" regardless of difficulty

- [x] **Fixes applied:**
  - Corrected difficulty ranges: Easy `1–20`, Normal `1–50`, Hard `1–100`
  - Swapped hint messages so they match the actual comparison direction
  - Changed `show_hint` default to `False`
  - Removed type-alternation logic; secret is always passed as an `int`
  - Initialized `attempts` to `0`
  - Added `st.session_state.status = "playing"` to the new game reset
  - Started score at `100` so penalties draw it down from a positive baseline
  - Simplified `Too High` branch to always subtract `5`
  - Updated info banner to use `{low}` and `{high}` from the difficulty range
  - Refactored all four logic functions (`get_range_for_difficulty`, `parse_guess`, `check_guess`, `update_score`) out of `app.py` into `logic_utils.py` using Claude Agent Mode

## 📸 Demo

