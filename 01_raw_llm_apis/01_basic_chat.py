# PHASE 1: Raw LLM APIs (Groq SDK)
# Task 1: Basic Chat Completion (01_basic_chat.py)
#
# Yahan aapko ek basic LLM API call implement karna hai.
# 
# Steps to follow:
# 
# 1. Sabse pehle zaroori packages import karein:
#    - load_dotenv ko 'dotenv' se (environment variables read karne ke liye)
#    - os (env vars retrieve karne ke liye)
#    - Groq ko 'groq' library se (official SDK client)
# 
# 2. environment variables load karein load_dotenv() call karke.
# 
# 3. .env file se "GROQ_API_KEY" variable get karein aur safety check lagayein ki key missing toh nahi hai.
# 
# 4. Groq client instance initialize karein API key pass karke:
#    client = Groq(api_key=your_api_key)
# 
# 5. client.chat.completions.create() ka use karke ek API request send karein:
#    - Model use karein: "llama-3.3-70b-versatile"
#    - Messages array define karein:
#      * System Message: Set karein ki model ek programming tutor hai jo answers ko 3 sentences me concise rakhta hai.
#      * User Message: Ek simple machine learning question puchein (e.g., "Why is Python so popular for ML?").
#    - Other parameters set karein:
#      * temperature=0.2 (taki response deterministic aur focused ho)
#      * max_tokens=150 (taki response length control me rahe)
# 
# 6. Response body se content extract karke console par print karein:
#    - Hint: response.choices[0].message.content
# 
# 7. Token usage metadata (Prompt Tokens, Completion Tokens, aur Total Tokens) print karein:
#    - Hint: response.usage.prompt_tokens, response.usage.completion_tokens, response.usage.total_tokens




from dotenv import load_dotenv
import os
from groq import Groq


load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if api_key is None:
    print("Groq API Key is not set. Please set it in the .env file.")
    exit()

client = Groq(api_key=api_key)

response = client.chat.completions.create(
    model = "llama-3.3-70b-versatile",
    messages = [
        {
            "role": "system",
            "content": "You are a programming tutor. Keep your answers concise, structured, and strictly within 3 sentences"
        },
        {
            "role": "user",
            "content":  "Why is Python so popular for ML?"
        }
    ],

    temperature = 0.2,
    max_tokens = 150
)

print(response.choices[0].message.content)

# Token which you sent to the model 
print(f"Prompt Tokens: {response.usage.prompt_tokens}")
# Token which model sent to you
print(f"Completion Tokens: {response.usage.completion_tokens}")
# Total token consumption 
print(f"Total Tokens: {response.usage.total_tokens}")


















































