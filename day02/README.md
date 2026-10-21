# AI Assistant with Context (Memory)

- How can an AI assistant know about the context in which you're asking a question?
  > Q: What's Python?
  > A: A **high-level, interpreted programming language** (meaning you can write code and run it directly, without compiling it first)
  > Q: Can you explain more about it?
  > A: ...

  - In the context above, what does "it" mean here? How can the model interpret "it" as "Python"?

- For that, you'd need to be able to store the conversation between you and the AI assistant, in some place.
  - For the most part, storing the conversation in a list works really well.
  - `messages.append({"role": "user", "content": user_input})`, where the `user_input` is the input message/prompt from the user in the conversation.

## `response` Object

- When you type in:

  ```py
  response = client.chat.completions.create(model=getenv("MODEL"), messages=messages)
  ```

  The `response` object can be taken a look into, as follows:

  ```py
  print(response.make_dump_json(indent=2))
  ```

  which might print something like the following:

  > {
  > "id": "chatcmpl-574",
  > "choices": [
  >     {
  >       "finish_reason": "stop",
  >       "index": 0,
  >       "logprobs": null,
  >       "message": {
  >         "content": "That's a great question! Python is one of the most popular and versatile programming languages in the world — **especially for beginners**. Here's a clear, concise breakdown of what makes Python special (with practical examples):\n\n---\n\n### ✅ **1. What is Python?**\n- A **high-level, interpreted programming language** (meaning you can write code and run it directly, without compiling it first).\n- Designed for **readability and simplicity** (uses clean, English-like syntax).\n- Supports **multiple programming paradigms**: \n  - Object-Oriented Programming (OOP)\n  - Procedural\n  - Functional\n  - Concurrent programming\n\n---\n\n### 🌟 **Why Python is So Popular** (Key Reasons)\n| Reason                  | Explanation                                                                 |\n|-------------------------|----------------------------------------------------------------------------|\n| 🐍 **Easy to Learn**    | Simple syntax (e.g., `print(\"Hello\")` vs. Java's `System.out.println(\"Hello\")`). Great for beginners. |\n| 🌐 **Versatile**        | Used in **web development** (Django/Flask), **data science** (Pandas, NumPy), **AI/ML** (TensorFlow, PyTorch), **scripting**, **automation**, **scientific computing**, and even **robotics**. |\n| 🛠️ **\"Batteries Included\"** | Built-in libraries for almost everything (e.g., `math`, `datetime`, `requests` for web APIs). |\n| 🐱 **Cross-Platform**   | Runs on Windows, macOS, Linux, and even embedded systems (e.g., Raspberry Pi). |\n| 🤖 **Industry-Standard** | Used by companies like Google, NASA, Netflix, Facebook, and countless startups.\n\n---\n\n### 🔧 **Real-World Example: \"Hello World\" in Python** (Super simple!)\n```python\nprint(\"Hello, World!\")\n```\n**Output**:  \n`Hello, World!`\n\n> ✨ **Why this works**: The `print()` function outputs text to the console. No complex setup — just write and run!\n\n---\n\n### 💡 **Python in Action** (Beyond \"Hello World\")\n| Use Case                | Example Library/Tool       | Real-World Example                                  |\n|-------------------------|-----------------------------|-----------------------------------------------------|\n| Data Analysis           | Pandas                      | Analyzing sales data for a business                 |\n| Web Development         | Flask/Django                | Building a website (e.g., Instagram, Reddit)         |\n| Artificial Intelligence | TensorFlow/PyTorch          | Training a model to recognize cats in photos         |\n| Automation              | `pyautogui`, `selenium`     | Automating browser tasks or file transfers          |\n| Scripting               | `subprocess`, `os`          | Automating repetitive tasks (e.g., backups)         |\n\n---\n\n### 🚫 What Python is **NOT**\n- **Not a compiled language** (unlike C/C++).  \n- **Not real-time programming** (uses interpreted code, so slower than compiled languages for strict timing systems).  \n- **Not for low-level hardware** (though it can be used in embedded systems via PyPy).\n\n---\n\n### 🌱 **Best for Who?**\n| Beginner | Intermediate | Expert |\n|----------|---------------|---------|\n| ✅ **Yes** (simple syntax) | ✅ (complex projects) | ✅ (AI/ML, systems) |\n\n> 💡 **Pro Tip for Beginners**: Start with **Python 3** (the current version). Avoid Python 2 (it's obsolete).\n\n---\n\n### 🔚 **Summary in 10 Words**\n> **\"Simple, powerful, and used everywhere — perfect for learning and real-world projects.\"**\n\n---\n\n### 🛠️ **Your First Step Today**\nTry this **real Python code** in your terminal (or any online Python editor like [Replit](https://replit.com)):\n\n```python\n# Print your name!\nprint(\"Hello, [Your Name]!\")\n```\n\nReplace `[Your Name]` with your actual name 👩‍💻\n\n---\n\n### 💬 Final Thought\n> *\"Python is the language that makes coding feel like playing with Lego — easy to start building, and you can create huge, complex structures.\"*  \n> — **Python's Creator Guido van Rossum**\n\nIf you're a beginner, **Python is your best friend**. If you have a specific interest (like web dev, data, or AI), I can give you targeted tutorials next! 😊\n\nLet me know what you'd like to explore next! 🚀",
  >         "refusal": null,
  >         "role": "assistant",
  >         "annotations": null,
  >         "audio": null,
  >         "function_call": null,
  >         "tool_calls": null,
  >         "reasoning": "Okay, the user just asked \"Hi, can you tell me about Python?\" – seems like a very open-ended beginner question. They're probably either a total newbie who wants a simple overview, or maybe someone with a bit of tech background wanting a refresher. \n\nHmm, I should avoid diving too deep into technical details upfront since they didn't specify their level. Better start with the absolute fundamentals: what it is, why it's popular, and maybe one concrete example to make it tangible. \n\n*checks mental notes* \nAh right – gotta emphasize the \"why\" for beginners. Like how Python's readability makes it great for learning, and how it's used in real stuff (web dev, data science etc.) to spark interest. Should mention the \"batteries included\" philosophy too – that's a cool unique trait. \n\nWait, they might be confused about Python vs other languages... better clarify it's not just \"another language\" but has this special balance of simplicity and power. Oh! And must include that \"hello world\" example – absolutely crucial for beginners to see it working. \n\n*thinks about pitfalls* \nDon't want to overwhelm them though. Skip advanced topics like decorators or concurrency. Focus on: \n- What it is (dynamic, interpreted, OOP) \n- Why it's awesome (simple syntax → fast learning) \n- Real-world uses (so they don't think it's just \"for homework\") \n- The hello world snippet to build confidence \n\n*double-checks* \nShould I mention Python 3 vs 2? ...Hmm, for a beginner that might confuse them more than help. Skip it unless they ask later. Focus on current Python 3. \n\n*imagines user's possible next steps* \nThey'll probably ask \"How do I start?\" next, so ending with \"Try making a 'hello world' program\" gives them a quick action to take. Smart to use the \"print\" function example – it's dead simple. \n\n...And definitely add that emoji at the end to keep it friendly. Newbies respond well to that warmth.\n"
  >       }
  >     }
  >   ],
  >   "created": 1792558565,
  >   "model": "qwen3:4b",
  >   "object": "chat.completion",
  >   "metadata": null,
  >   "moderation": null,
  >   "service_tier": null,
  >   "system_fingerprint": "fp_ollama",
  >   "usage": {
  >     "completion_tokens": 1387,
  >     "prompt_tokens": 19,
  >     "total_tokens": 1406,
  >     "completion_tokens_details": null,
  >     "prompt_tokens_details": null
  >   }
  > }

## How does memory in a conversation work?

- The `response.choices[0].message` object can be directly stored in `messages` list in our program, to save the context of the conversation, as follows:

  ```py
  messages.append(response.choices[0].message)
  ```

- Rest of the handling of a correct response will be taken care of, inside the `while True:` infinite loop, as we've the following line:

  ```py
  client = OpenAI(base_url=os.getenv("BASE_URL"), api_key=os.getenev("API_KEY"))

  # 0. Store the entire conversation inside the messages[] list.
  messages = []

  while True:
    # 1. User Raw Input
    # 2. User Input Sanitization
    # 3. Check if user wants to exit the conversation

    # 4. Append the current user input into messages[]
    messages.append({"role": "user", "content": user_input})

    # 5. Send the request to the AI model, with the entire conversation of messages[] till now
    response = client.chat.completions.create(model=getenv("MODEL"), messages=messages)

    # 6. Store the response's message into the messages[] again, because the AI model must remember the context the next time the client.chat.completions.create() is called again.
    messages.append(response.choices[0].message)

    # 7. Print the response's message content
    print(response.choices[0].message.content)
  ```
