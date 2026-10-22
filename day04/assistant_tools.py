from openai import OpenAI
from dotenv import load_dotenv
from os import getenv, get_terminal_size
from random import randint
from tools import get_current_time, roll_dice, generate_password

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

    words_in_user_sanitized_prompt = set(user_sanitized_prompt.split())

    if words_in_user_sanitized_prompt & TOOL_WORDS['time']:
        print(f"\n🤖> Current time is: {get_current_time()}")
        print(SEPARATOR)
        continue

    if words_in_user_sanitized_prompt & TOOL_WORDS['dice']:
        print(f"\n🤖> Rolled a dice, and you got: {roll_dice()}")
        print(SEPARATOR)
        continue

    if words_in_user_sanitized_prompt & TOOL_WORDS['password']:
        pass_len = randint(12, 30)
        print(
            f"\n🤖> Generating a random password of length {pass_len}: {generate_password(pass_len)}")
        print(SEPARATOR)
        continue

    messages.append({"role": "user", "content": user_raw_prompt})

    response = client.chat.completions.create(model=MODEL, messages=messages)

    messages.append(response.choices[0].message.model_dump())

    print(f"\n🤖> {messages[len(messages) - 1]['content']}")
    print(SEPARATOR)
