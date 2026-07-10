# PHASE 1: Raw LLM APIs (Groq SDK)
# Task 2: Real-time Response Streaming (02_streaming_chat.py)
#
# Yahan aapko response ko word-by-word (token-by-token) stream karna seekhna hai.
# 
# Steps to follow:
# 
# 1. Imports setup karein:
#    - Groq client package, load_dotenv, os.
#    - 'sys' import karein taaki hum stdout stream me characters bypass kar sakein.
# 
# 2. Env se GROQ_API_KEY retrieve karke client instance banayein.
# 
# 3. Chat completion request create karein:
#    - Model: "llama-3.3-70b-versatile"
#    - User message: Kisi creative/funny topic pe paragraph write karne bolein (e.g., "Explain why programmers love coffee in a funny way").
#    - Parameters: stream=True pass karein (yeh model output ko stream me divide karega).
# 
# 4. Ab output stream ko iterate karein:
#    - Loops lagayein: 'for chunk in response:'
#    - Har chunk se incremental text content check karein: chunk.choices[0].delta.content
#    - Agar content valid hai (not None), toh use bina extra spaces/newlines ke print karein.
#      * Hint: sys.stdout.write(content) use karein aur stream buffer clear karne ke liye sys.stdout.flush() karein.
# 
# 5. Loop complete hone ke baad ek empty print() execute karein line break ke liye.

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













































