import google.generativeai as genai
import os
import EnvironmentVariables
from mongoDBConnection import DBConnection

class Chat:
    def __init__(self):
        genai.configure(api_key=EnvironmentVariables.gemini_api_key)
        self.model = genai.GenerativeModel(
            model_name=EnvironmentVariables.model,
            system_instruction=EnvironmentVariables.instruction
        )
    
    def call_llm_api(self, prompt):
        response = self.model.generate_content(prompt)
        #print(response.text)
        return response.text
    
    def search_knowledge_base(self, query):
        connection = DBConnection()
        result = connection.getResult(query)
        if result:
            return result["definition"]
    
    def generate_response(self, query):
        response = self.search_knowledge_base(query)
        if response:
            prompt = "Sử dụng thông tin sau đây để trả lời câu hỏi.\n"
            prompt += f"Dữ liệu: {response}\nCâu hỏi: {query}"
            return self.call_llm_api(prompt)
        else:
            return self.call_llm_api(query)
    
# def main():
#     s = input("Please enter your question: ")
#     chatbot = Chat()
#     print(chatbot.call_llm_api(s))
    
# if __name__ == "__main__":
#     main()