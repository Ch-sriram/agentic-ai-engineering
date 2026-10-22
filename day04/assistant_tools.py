from openai import OpenAI
from dotenv import load_dotenv
from os import getenv, get_terminal_size
from tool_manager import execute_tool

load_dotenv()
BASE_URL = getenv("BASE_URL")
API_KEY = getenv("API_KEY")
MODEL = getenv("MODEL")

columns, _ = get_terminal_size()
SEPARATOR = "\n" + ('-' * columns) + "\n"
BYE_MSG = "🤖> Bye, let's meet again!\n"
CONV_HIST = "Conversation History"

print(SEPARATOR)
print(f"Welcome, I'm your AI Assistant. I'm ready to help!")
print(f">> Type in 'quit' / 'bye' / 'exit' to quit.")
print(f">> Type in '/h' or '/history' for displaying the conversation history.")
print(SEPARATOR)

client = OpenAI(base_url=BASE_URL, api_key=API_KEY)

EXIT_PROMPTS = ("exit", "bye", "quit")
HISTORY_PROMPTS = ("/h", "/history")
TOOL_WORDS = {
    "time": {"time", "clock"},
    "dice": {"dice", "die"},
    "password": {"password", "passcode"}
}

messages = []

while True:
    user_raw_prompt = input("> ")
    user_sanitized_prompt = user_raw_prompt.lower()

    if user_sanitized_prompt in EXIT_PROMPTS:
        print(BYE_MSG)
        break

    if user_sanitized_prompt in HISTORY_PROMPTS:
        print(CONV_HIST)
        print('-' * len(CONV_HIST))

        if len(messages) == 0:
            print('nil')
        else:
            for msg_obj in messages:
                print(f"{msg_obj['role'].title()}: {msg_obj['content']}")

        print(SEPARATOR)
        continue

    tool_response = execute_tool(user_sanitized_prompt)
    if tool_response != None:
        print(tool_response + SEPARATOR)
        continue

    messages.append({"role": "user", "content": user_raw_prompt})

    response = client.chat.completions.create(model=MODEL, messages=messages)

    messages.append(response.choices[0].message.model_dump())

    print(f"\n🤖> {messages[len(messages) - 1]['content']}")
    print(SEPARATOR)
