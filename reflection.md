# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

  a. When the Secret was 65 and I typed in 50 the message that popped up was misleading as it asked me to go lower
  b. History was not being recorded correctly, it was not making a correct list of my guesses.
  c. New game button does not renew attempts left

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| 50    |  Go Higher!         Go Lower!         Wrong message displayed
|   26  |   { 26:1 }            {  }            History not tracked properly
| 40    | go higher/lower!   no attempts left   New game button doesnt reset attempts.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

I exclusively used the VS Code AI Assistant. The correct suggestion that AI gave me was to change the code for the check guess feature so that the messages are right. The incorrect suggestion it gave me was for the import statements that was used to pull different files in logic_utils.py which was unnecessary since we import thr functionalities in app.py.

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

I determined that the bug was fixed using in game testing. I went to the server and checked myself to make sure that the game was running as intended after the fixes done by AI. One test that I ran was for the reset button, which verified that the all variable values pertaining to the game was updated once it was clicked. AI had helped me reset all variables to its initial state and test it in the test file,

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
