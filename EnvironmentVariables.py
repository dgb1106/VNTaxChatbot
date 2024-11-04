from dotenv import load_dotenv
import os

load_dotenv()

gemini_api_key = os.getenv("API_KEY")
default_language = os.getenv("DEFAULT_LANGUAGE")

print("API_KEY:", gemini_api_key)
print("DEFAULT_LANGUAGE:", default_language)