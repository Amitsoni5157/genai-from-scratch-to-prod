# PHASE 1: Raw LLM APIs (Groq SDK)
# Task 3: Structured Outputs & validation (03_structured_outputs.py)
#
# Yahan aap seekhenge ki LLM se strictly formatted JSON output lekar use Pydantic se kaise validate karte hain.
# 
# Steps to follow:
# 
# 1. Imports setup karein:
#    - json, os, Groq SDK.
#    - Pydantic se BaseModel, Field aur ValidationError import karein.
#    - Typing modules se List import karein.

from pydantic import ValidationError
import json
import os
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from groq import Groq

# 2. Pydantic schema class banayein:
#    - Class name 'UserProfile' (inherit from BaseModel).
#    - Schema parameters: name (str), age (int), skills (List[str]), aur current_role (str).
#    - Field parameters use karke descriptions add karein taaki data clear ho. 


# define pydantic schema for the structured output
class UserProfile(BaseModel):
    name: str = Field(..., description="Full name of the user")
    age: int = Field(..., description="Age of the user")
    skills: list[str] = Field(..., description="List of skills of the user")
    current_role: str = Field(..., description="Current role of the user")

# 3. Environment load karke client instantiate karein.
load_dotenv()

# load your env variables 
api_key = os.getenv("GROQ_API_KEY")

# initialize the client
client = Groq(api_key = api_key)

# 
# 4. Ek raw unstructured string variable define karein:
#    raw_text = "Hi, I am Rohit. I work as a Python Developer, age 28. I know Python, Git, and FastAPI."

raw_text = "Hi, I am Rohit. I work as a Python Developer, age 28. I know Python, Git, and FastAPI."

# 5. API call invoke karein:
#    - Model: "llama-3.3-70b-versatile"
#    - System Prompt: Instructions dein ki bot information extract kare aur strict JSON output de. No explanations, no backticks.
#    - User Prompt: f"Extract name, age, skills, and current_role from: {raw_text}"
#    - IMPORTANT: parameters me `response_format={"type": "json_object"}` pass karein. JSON mode activate karne ke liye prompt me 'JSON' word likhna zaroori hai.
response = client.chat.completions.create(
    model = "llama-3.3-70b-versatile",
    messages =[
        {
            "role": "system",
            "content": "You are a data extraction assistant. Extract information and return only a JSON object."
        },
        {
            "role": "user",
            "content": f"Extract name, age, skills, and current_role from: {raw_text}"
        }
    ],
    response_format = {"type": "json_object"}
)



# 6. Response capture karke raw string print karein console par.
raw_response = response.choices[0].message.content
print("Raw Response:", raw_response,"\n")
print("Type of raw response : ", type(raw_response),"\n")

# 7. Try-Except block setup karein:
#    - json.loads() se string content ko python dict me convert karein.
#    - UserProfile(**your_dict) calling se validation check karein.
#    - Validated data properties print karein.
#    - Exceptions handle karein: JSONDecodeError (agar model input invalid JSON thi) aur ValidationError (agar key missing ya data type error tha).
try:
    data = json.loads(raw_response)
    print("Data:", data,"\n")
    print("Type of data : ", type(data),"\n")

    profile = UserProfile(**data)
    print("Profile:", profile,"\n")
    print("Type of profile : ", type(profile),"\n")
    print(f"Name: {profile.name}, Age: {profile.age}")

except ValidationError as e:
    print(f"Validation Error:",e)
except json.JSONDecodeError:
    print("Invalid JSON returned by LLM.")
