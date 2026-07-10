from os import truncate
from dotenv import load_dotenv
import os
from groq import Groq
import sys

# load env vars 
load_dotenv()
# get your API key 
api_key = os.getenv("GROQ_API_KEY")

if api_key is None:
    print("Error: API Key not found. Set GROQ_API_KEY in .env")
    exit()

# initlize the client 
client = Groq(api_key = api_key)

# call the LLM model with stream = True 
response = client.chat.completions.create(
   model="llama-3.3-70b-versatile",
   messages=[
        {
            "role": "user",
            "content": "Explain why programmers love coding in a funny way"
        }
   ],
   stream = True
)

# Iterate through the response and print the content
for chunk in response:
    # get the content from the chunk
    content = chunk.choices[0].delta.content
    # if content is not None: # check if the content is not None
    if content is not None:
        # use sys.stdout.write(content) to print the content without extra spaces/newlines
        sys.stdout.write(content)
        # use sys.stdout.flush() to clear the stream buffer
        sys.stdout.flush()

# print an empty line after the response
print()













































