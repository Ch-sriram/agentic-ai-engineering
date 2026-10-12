from openai import OpenAI
from dotenv import load_dotenv
from os import getenv, get_terminal_size

# Load the .env variables, so that the OS module can recognize those variables
load_dotenv()

# Create a client to communicate with Ollama
client = OpenAI(base_url=getenv("BASE_URL"), api_key=getenv("API_KEY"))

columns, _ = get_terminal_size()

print(columns * "=")
print(" My Personal AI Assistant (type 'quit' or 'bye' to exit)")
print(columns * "=")

# We want the conversational loop to keep on going, until user exits
while True:
    user_raw_input = input("\n> ")
    user_prompt = user_raw_input.lower()

    if user_prompt == "quit" or user_prompt == "bye":
        print("Bye! See you next time...\n")
        break

    messages = [{"role": "user", "content": user_raw_input}]

    response = client.chat.completions.create(
        model=getenv("MODEL"), messages=messages)

    print("\n🤖> " + response.choices[0].message.content + "\n")
