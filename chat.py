import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")
instruction = os.getenv("INSTRUCTION")

class Chat:
    def __init__(self):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            system_instruction=instruction
        )
    
    def call_llm_api(self, question):
        response = self.model.generate_content(question)
        #print(response.text)
        return response.text
    
# def main():
#     s = input("Please enter your question: ")
#     chatbot = Chat()
#     print(chatbot.call_llm_api(s))
    
# if __name__ == "__main__":
#     main()