from openai import OpenAI
from dotenv import load_dotenv
from os import getenv, get_terminal_size

# Load the environment variables in .env file in this venv
load_dotenv()

# Create a client using OpenAI's APIs
client = OpenAI(base_url=getenv("BASE_URL"), api_key=getenv("API_KEY"))

# Create a list for storing all conversation history.
# - Ensure that the first stored conversation is a "system" prompt that tells
#   the assistant how to behave by default.
messages = [
    {
        "role": "system",
        "content": "You're a friendly AI teacher. Explain every concept in a simple language, with real-life examples."
    }
]

exit_prompts = ("exit", "bye", "quit")
history_prompts = ("/h", "/history")
CONV_HIST = "Conversation History"
BYE_MSG = "Bye, see you again!"

columns, _ = get_terminal_size()
print('=' * columns)
print(
    "My Personal AI Assistant ('bye' / 'quit' / 'exit' to exit) ['/h' / '/history' for conversation history]")
print('=' * columns)

while True:
    user_raw_prompt = input("> ")
    user_sanitized_prompt = user_raw_prompt.lower()

    if user_sanitized_prompt in exit_prompts:
        print(BYE_MSG)
        break

    if user_sanitized_prompt in history_prompts:
        print('\n' + CONV_HIST)
        print("-" * len(CONV_HIST))
        if len(messages) == 0:
            print('nil')
        else:
            for message_object in messages:
                print(
                    f"{message_object['role'].title()}: {message_object['content']}")
        print('\n' + ('-' * columns) + '\n')
        continue

    messages.append({"role": "user", "content": user_raw_prompt})
    response = client.chat.completions.create(
        model=getenv("MODEL"), messages=messages)

    # Store the response in the conversation history list
    messages.append(response.choices[0].message.model_dump())

    # Print the response from the model
    print("\n🤖> " + messages[len(messages) - 1]['content'])
    print('\n' + ('-' * columns) + '\n')
