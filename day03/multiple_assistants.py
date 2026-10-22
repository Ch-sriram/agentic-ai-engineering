from openai import OpenAI
from dotenv import load_dotenv
from os import getenv, get_terminal_size

load_dotenv()

client = OpenAI(base_url=getenv("BASE_URL"), api_key=getenv("API_KEY"))

MODEL = getenv("MODEL")
DEFAULT_ROLE_TITLE = MODEL.upper()
DEFAULT_ROLE = "You're an AI Assistant!"

roles = {
    "1": "You're a friendly AI teacher. Explain every concept in a simple language, with real-life examples.",
    "2": "You're a Senior Software Engineer who's an expert in any programming language. Explain every programming concept with real-life examples.",
    "3": "You're a Travel Guide who has been to many places in the world. Your job is to explain the most visited spots for the best user experience, given a travel destination.",
    "4": "You're a Motivational Coach. Make positivity the Mantra of life, and make sure that the user learns something about themselves they forgot/didn't-know. Ensure that the user is motivated to do what they want to achieve",
    "5": "You're an Interviewer whose job is to ask questions on the topic of choice the user wants to be interviewed on. You give a question from the chosen topic, and then the user answers them. The questions must increase in difficulty as the interview goes longer.",
    "6": "You're an experiences legal advisor. Explain legal concepts in a simple language, but never claim to provide formal legal advice.",
    "7": "You're a Michelin Star Chef who knows how to cook various dishes from around the world. Explain recipes and dishes in a simple language, and why a specific ingredient is added into the dish.",
    "8": "You're an experienced Fitness Trainer who has trained many people, and helped them become fitter in their lives. Explain exercise routines in a simple language, and ensure that you ask the user to seek a doctor/physio for any advice related to injuries",
    "9": "You're a Career Counselor who understands every career in-depth, and what all entails to be able to choose that career. Explain the career-path in a simple language, and refrain from giving bad advice."
}

roles_title = {
    "1": "Teacher",
    "2": "Programming Expert",
    "3": "Travel Guide",
    "4": "Motivational Coach",
    "5": "Interviewer",
    "6": "Legal Advisor",
    "7": "Chef",
    "8": "Fitness Trainer",
    "9": "Career Counselor",
}

print("""
Choose Your AI Assistant:
  1. Teacher
  2. Programming Expert
  3. Travel Guide
  4. Motivational Coach
  5. Interviewer
  6. Legal Advisor
  7. Chef
  8. Fitness Trainer
  9. Career Counselor
""")

choice = input("\n> Enter Your Choice of AI Assitant: ")
print(f"> Your Choice: {choice}")
columns, _ = get_terminal_size()
SEPARATOR = '-' * columns

system_role = roles.get(choice, DEFAULT_ROLE)
system_role_title = roles_title.get(choice, DEFAULT_ROLE_TITLE)

print("\n" + SEPARATOR)
print(
    f"Welcome, I'm your {system_role_title} AI Assistant. I'm ready to help!")
print(f">> Type in 'quit' / 'bye' / 'exit' to quit.")
print(f">> Type in '/h' or '/history' for displaying the conversation history.")
print("\n" + SEPARATOR + "\n")

messages = [
    {
        "role": "system",
        "content": system_role
    }
]

EXIT_PROMPTS = ("exit", "bye", "quit")
HISTORY_PROMPTS = ("/h", "/history")
BYE_MSG = "Bye, let's meet again!"
CONV_HIST = "Conversation History"

while True:
    user_raw_prompt = input("\n> ")
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
            for message_object in messages:
                print(
                    f"{message_object['role'].title()}: {message_object['content']}")

        print("\n" + SEPARATOR)
        continue

    messages.append({"role": "user", "content": user_raw_prompt})

    response = client.chat.completions.create(
        model=MODEL, messages=messages)

    messages.append(response.choices[0].message.model_dump())

    print(f"\n🤖> {messages[len(messages) - 1]['content']}")
    print("\n" + SEPARATOR + "\n")
