import os
from dotenv import load_dotenv

load_dotenv()
openai_api_key = os.getenv("openai_api_key")
print(f"OpenAI API Detected: {'Yes' if os.getenv("openai_api_key") else 'No'}")
