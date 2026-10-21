from openai import OpenAI
from dotenv import load_dotenv
from os import getenv, get_terminal_size

# Load .env file's environment variables to be accessible by os.getenv
load_dotenv()

# Create an OpenAI client, using the loaded environment variables
client = OpenAI(base_url=getenv("BASE_URL"), api_key=getenv("API_KEY"))

# Make total number of columns using os.get_terminal_size
columns, _ = get_terminal_size()

print(columns * "=")
print(" My Personal AI Assistant + Memory (type 'quit' / 'bye' / 'exit' to exit)")
print(columns * "=")

# Create an empty list to ensure that the entire conversation is stored.
messages = []

while True:
    user_raw_input = input("\n> ")
    user_prompt = user_raw_input.lower()

    exit_prompts = ["quit", "bye", "exit"]

    if user_prompt in exit_prompts:
        print("Bye! See you next time...\n")
        break

    # Append the user's raw input into the message with a "user" role,
    # since this was actually asked by the user.
    messages.append({
        "role": "user",
        "content": user_raw_input
    })

    # Send all the messages till now, to the AI model.
    # The AI model can now understand the entire context of the conversation
    # everytime the user starts prompting.
    response = client.chat.completions.create(
        model=getenv("MODEL"), messages=messages)

    # print(response.model_dump_json(indent=2)) # Debug statement

    # Append the response into the `messages[]` list.
    messages.append(response.choices[0].message)

    # In some cases, the entire `response.choices[0].message` is too large,
    # so only store the message content as follows:
    # messages.append({"role": "assistant", "content": response.choices[0].message.content})

    print("\n🤖> " + response.choices[0].message.content + "\n")
    print(columns * '-')
