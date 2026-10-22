# Teach Your AI Assistant How to Behave

- Same question, depending on who's answering, can change the answer drastically.
- For example, if the question is the following:
  > Q: What is AI?
  - Teacher's Perspective:
    > A field that builds machines capable of performing tasks associated with intelligence.
  - Lawyer's Perspective:
    > A technology that creates new questions about accountability, rights, and responsibility.
  - Comedian's Perspective:
    > A machine that can write a PhD thesis but might still confidently get your birthday wrong.
  - Software Engineer's Perspective:
    > Computational systems that learn patterns, make predictions, or generate outputs.
  - Philosopher's Perspective:
    > A challenge to our understanding of intelligence, consciousness, and human uniqueness.
  - Businessperson's Perspective:
    > A tool for automation, productivity, decision support, and value creation.
- If we want our assistant to behave as specfic type of person; teacher, lawyer, comedian, software engineer, philosopher, busenessperson, etc, we have to change the `role` given in `message` object.
- The specific `role` used is `system`.

## What is a System Prompt?

- A system prompt is a set of instructions that tells the AI:
  1. Who are you?
  2. How should you behave?
  3. What tone should you use?
  4. What should you avoid?
  5. Who is your audience?
- Unlike user messages, the __system prompt__ isn't part of the conversation.
  - Instead, it acts like a set of permanent instructions that guide every response.
- System prompts can be simplified to be __AI's Job Description__.

## Example of a Good System Prompt

Prompt:

> - You are an experienced Python trainer.
> - Explain programming concepts in simple language.
> - Always include one Python example.
> - Keep answers under 200 words.
> - Encourage beginners.
