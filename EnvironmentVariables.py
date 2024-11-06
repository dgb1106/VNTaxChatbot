from dotenv import load_dotenv
import os

load_dotenv()

gemini_api_key = os.getenv("API_KEY")
model = os.getenv("MODEL")
default_language = os.getenv("DEFAULT_LANGUAGE")
instruction = os.getenv("INSTRUCTION")
mongodbURI = os.getenv("MONGODB_URI")

# print("API_KEY:", gemini_api_key)
# print("MODEL:", model)
# print("DEFAULT_LANGUAGE:", default_language)
# print("MONGODB_URI:", mongodbURI)