# Agentic AI Engineering &mdash; Building Production-Ready AI Agents

- An AI Agent is simply an AI Assistant with additional benefits such as:
  1. Planning
  2. Using Tools
  3. Memory - Remembering Information
  4. Taking Actions

## Table of Contents

- [What is an AI Model?](#what-is-an-ai-model)
  - [Where does the AI model(s) Run?](#where-does-the-ai-models-run)
  - [What We Need for Agentic Engineering?](#what-we-need-for-agentic-engineering)
  - [How to Install Ollama?](#how-to-install-ollama)
    - [Why Qwen3?](#why-qwen3)
    - [Run Qwen3](#run-qwen3)

## What is an AI Model?

1. An AI Model is the "brain" of your assistant.
2. It has already learned from enormous amounts of text, books, articles, websites, and publicly available information.
3. When you as a question, the model predicts the most appropriate response based on what it has learned.
4. You don't need to know how the model was trained to build useful AI applications. When using AI models, the focus should be pertained to how efficiently to make use of the AI models, rather than training them.

### Where does the AI model(s) Run?

- There are _two_ common options:
  1. Cloud Models &mdash; models that are hosted on cloud:
     - The AI model runs on someone else's serviers, and your program sends requests over the internet.
     - Examples include models from OpenAI, Google, Anthropic, XAi, etc.
  1. Local Models &mdash; The AI model runs directly on your own computer.
     - Ollama is used as an open source model maintainer, and mose of the models that are downloadable from Ollama, are:
       1. Free
       1. Private
       1. Easy to install
       1. Great for learning
       1. Incur no API charges

[ꜛ️](#table-of-contents)

### What We Need for Agentic Engineering?

1. Python &mdash; Programming Language
2. Visual Studio Code &mdash; Code Editor
3. Ollama &mdash; Runs AI models on your computer
4. Git (Optional) &mdash; Version Control

> Find out how to install the aforementioned, using any LLM of your choice.

[ꜛ️](#table-of-contents)

### How to Install Ollama?

- Ollama makes running open-source AI models incredibly simple.
- Download Qwen 3 (4B), because it provides a good balance between speed and quality on most modern machines.

  ```sh
  # Pull qwen3 which loads 4b parameters once loaded
  ollama pull qwen3:4b

  # If you want a smaller version of qwen3, you can pull qwen3:1.7b
  ```

#### Why Qwen3?

- Qwen3 is lightweight, open-source, and runs well on everyday hardware.
- If a newer better model becomes widely availble in the future, we can simply replace the model name without changing the rest of the code.

#### Run Qwen3

- Use the following command:

  ```sh
  # List the models that you've downloaded till now.
  ollama list

  # Run the qwen3:4b model in your machine
  ollama run qwen3:4b

  # Once inside, you can type in `/bye/`, or Ctrl+C to exit
  ```

  > You should be able to interact with the model.

[ꜛ️](#table-of-contents)

#### Create a Python Virtual Environment

- Create a python virtual environment, and name the directory that stores the library as `.venv`:

  ```sh
  python -m venv .venv
  ```

- Activate the virtual environment, using the `activate` script either inside `.venv/bin/`, or inside `.venv\Scripts\`:

  ```sh
  source .venv/bin/activate
  ```

- If activate correctly, you should see something like `(.venv)` in your terminal prompt, at the beginning.
- To come out of the virtual environment, just type in `deactivate` in your terminal.
