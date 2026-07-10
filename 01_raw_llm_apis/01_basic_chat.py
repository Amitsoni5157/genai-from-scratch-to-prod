from dotenv import load_dotenv
import os
from groq import Groq


# load your env variables 
load_dotenv()

# get your api key
api_key = os.getenv("GROQ_API_KEY")

# safety check 
if api_key is None:
    print("Groq API Key is not set. Please set it in the .env file.")
    exit()

# initlize your client 
client = Groq(api_key=api_key)

# call your LLM model
response = client.chat.completions.create(
    # which model you want to use 
    model = "llama-3.3-70b-versatile",
    messages = [
        # system prompt : sets the behavior of the model 
        {
            "role": "system",
            "content": "You are a programming tutor. Keep your answers concise, structured, and strictly within 3 sentences"
        },
        # user message : the actual prompt you send to the model 
        {
            "role": "user",
            "content":  "Why is Python so popular for ML?"
        }
    ],
    # set the temperature of the model (creativity)
    temperature = 0.2,
    # set the max tokens of the model (length of response)
    max_tokens = 150
)

# print the response 
print(response.choices[0].message.content)

# Token which you sent to the model 
print(f"Prompt Tokens: {response.usage.prompt_tokens}")
# Token which model sent to you
print(f"Completion Tokens: {response.usage.completion_tokens}")
# Total token consumption 
print(f"Total Tokens: {response.usage.total_tokens}")


















































