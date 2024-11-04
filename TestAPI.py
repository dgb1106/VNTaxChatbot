import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")
instruction = os.getenv("INSTRUCTION")

genai.configure(api_key=api_key)
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction=instruction
)

def call_llm_api(question):
    response = model.generate_content(question)
    print(response.text)

def main():
    s = input("Please enter your question:")
    call_llm_api(s)
    
if __name__ == "__main__":
    main()