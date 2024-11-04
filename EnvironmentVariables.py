from dotenv import load_dotenv
import os

load_dotenv()

gemini_api_key = os.getenv("API_KEY")

print("API_KEY:", gemini_api_key)