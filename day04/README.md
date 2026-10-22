# AI w/ Tool Usage

- If I've _two_ kinds of assistants:
  - _Assistant A_: Can answer questions.
  - _Assistant B_: Can answer questions, and use tools.
- In any scenario, _Assistant B_ is preferred over _Assistant A_:
  > _Assistant B_ >> _Assistant A_

## Why AI w/ Tool Usage?

- Image the following conversations:
  1. What's `345 * 876`?
     > The AI answers correctly.
  1. What's the current time?
     > The AI answers again, correctly.

  In both the scenarios, how does AI know what the correct answer is?
  > Does AI have a calculator, and a clock inside it? NO!

  1. Generate a secure random password.
     > AI answers, but does it actually have a secure password generator, or is it simply making up something that looks like a password?

  1. Roll a dice.
     > AI answers with a random answer between 1-6. But does AI truely knows what true randomness is? Not really!

  1. Read the contents of `notes.txt`.
     > Can the AI model, as it is, open the files stored on your computer? NO!

- In all the scenarios aforementioned, something is missing!
- An AI model is excellent at:
  - Explaining
  - Writing
  - Reasoning
  - Summarising
  - Translating
  - Brainstorming
- But there are things it cannot do by itself, like:
  - Read your local files
  - Check your computer's clock
  - Open a web browser
  - Perform guaranteed accurate calculations
  - Access your database
  - Send emails
  - Control your applications

## What is an AI Tool?

- AI makes use of tools, just like a human does, to do something which is quantifiable by nature.
- An AI Tool is simple a piece of software that performs a specific task. Examples include:
  - Calculator
  - Clock
  - Calendar
  - Web Browser (Search Engine)
  - PDF Reader
  - Database
  - Camera
  - GPS
  - Email Client
  > We can make our AI assistants to learn these tools, same as how humans use them daily.

## Distinction between AI & AI Tools?

- The AI model doesn't become better at math because we give it a calculator, instead, the AI becomes smart enough to know: "I should use the calculator" for this prompt.
- Similarly, the AI model doesn't become better at telling time, it simple learns when: "I should ask the system clock".
- This distinction is important:
  - AI Model => Reasoning
  - Tasks => Tools

## How to make AI Tools?

- We create a file named `tools.py`.
- As our project grows, we'll have many tools, and instead of putting everything into one large file, we'll organize our code into modules.

### Creating the "Current Date & Time" Tool

- In `tools.py`, define a method that gets current date and time:

  ```py3
  from datetime import datetime

  def get_current_time():
    """Return the current date and time."""

    return datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")
  ```

- We've to test the tool that we just created:
  - Create a file named `test_tools.py` as follows:

    ```py
    from tools import get_current_time # We're import `get_current_time` method from inside tools.py file
    print(get_current_time()) # This should print the current time, correctly.
    ```
  
  - Testing a tool is important because:
    1. Professional developers test small pieces before combining them into larger piece of software.

### Creating the "Dice Roller" Tool

- In `tools.py`, define a method that returns a random die roll from \[1-6\]:

  ```py
  import random

  def roll_dice():
    """Return a random number between 1 and 6."""

    return random.randint(1, 6)
  ```

## Connecting Tools to AI Assistant

- User Question/Prompt:
  - Can Python handle this?
    - Yes: Use a Tool
    - No: Pass it to the underlying AI model

- In `assistant.py`, import the methods from `tools.py`:

  ```py
  from tools import get_current_time, roll_dice, generate_password

  # ...
  # ...
  if "time" in user_input.lower():
    print("\nAI: ", get_current_time())
    continue
  
  # The AI model is never called
  ```

- To add support for rolling a dice, do the following:

  ```py
  
  if "dice" in user_input.lower():
    print("\nAI: You rollled a ", roll_dice())
    continue
  ```
