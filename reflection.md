# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

The game looked normal when I first ran it. Just told me to guess a number between 1 and 100 with a certain number of attempts.

The first bug I noticed was that with every number I tried it just kept telling me to 'go lower'. Eventually it let me get to 0. 

The second concrete bug I found was that when I would try to start a new game it did not let me. 

Other bugs: 
- the ranges dont change based on the difficulty level 
- state problems?? idk someone said that, i might have to check.
- can get a negative score

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?

    I used ClaudeCode in VSCode

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

    One example was that it found that the go higher and go lower hints were inverted. I verified this by retesting the game. 

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

    the ai thought one of the issues was that the hint is only wrong on even numbered attemps and correct on odd, but really its that the output got switched (ex: when it says 'go higher' it really means 'go lower')


---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
    I decided the bug was fixed by reading the logic carefully and tracing through what the code actually does    

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
    I manually tested by opening the Developer Debug Info panel in the app to see the secret number, then entering a number I knew was lower than it — before the fix it still said "Go LOWER", but after the fix it correctly said "Go HIGHER", confirming the messages were swapped.


- Did AI help you design or understand any tests? How?
     Yes — Claude Code helped identify the bugs by reading the source code and explaining exactly what was going wrong, which showed me what specific inputs to use when manually testing (like guessing below the secret to verify the hint direction).


---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.

  Every time Streamlit reruns the page (which happens on every button click or input), it re-executed random.randint() to generate a new secret because there was no check to see if one had already been saved.

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

  Every time you interact with a Streamlit app — clicking a button, typing in a box — the entire Python script runs again from top to bottom; session state is like a small notepad that remembers values between those reruns so things like your score or the secret number don't get wiped out each time.

- What change did you make that finally gave the game a stable secret number?

  Wrapping the secret generation in if "secret" not in st.session_state means the random number is only generated once — on the very first run — and from then on Streamlit just reads the saved value from session state instead of creating a new one.


---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.

   I want to keep using the Developer Debug Info panel (or print statements) to expose hidden state like the secret number, because being able to see what the code is actually doing made bugs much easier to spot and confirm.

- What is one thing you would do differently next time you work with AI on a coding task?

I would read through the AI-generated code more carefully before running it, so I can catch obvious logic errors like swapped messages or missing resets before they become confusing bugs in a live game.

- In one or two sentences, describe how this project changed the way you think about AI generated code.

AI can write code that looks correct and runs without errors but still has subtle logic bugs, so I now treat AI code as a starting point that needs to be tested and verified, not a finished product.