from openai import OpenAI
from dotenv import load_dotenv
import os

# Load the environment variables from `.env` file.
load_dotenv()

# Create a client that communicates with Ollama
client = OpenAI(
  base_url=os.getenv("BASE_URL"),
  api_key=os.getenv("API_KEY")
)

messages = [
  {
    "role": "user", # This is coming from the user, not from another model
    "content": "Write a poem about rain."
  }
]

# Send a question to the AI model, we can dynamically take in the `content`
# part of the messages, from the user.
response = client.chat.completions.create(
              model=os.getenv("MODEL"),
              messages=messages)

# The AI model responds a lot of information, which can be seen by printing the response
print(response)

# The actual information exists at:
print(response.choices[0].message.content)
