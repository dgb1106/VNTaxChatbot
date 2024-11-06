import google.generativeai as genai
import os
import EnvironmentVariables
from mongoDBConnection import DBConnection

import textwrap

class Chat:
    def __init__(self):
        genai.configure(api_key=EnvironmentVariables.gemini_api_key)
        self.model = genai.GenerativeModel(
            model_name=EnvironmentVariables.model,
            system_instruction=EnvironmentVariables.instruction
        )
        
    def to_markdown(self,text):
        text = text.replace('•', '  *')
        return textwrap.indent(text, '> ', predicate=lambda _: True)
    
    def call_llm_api(self, prompt, temp):
        temp /= 50
        response = self.model.generate_content(prompt, 
            generation_config=genai.types.GenerationConfig(
                temperature=temp
            )
        )
        # print(response.text)
        # print(temp)
        response_markdown = self.to_markdown(response.text)
        return response_markdown
    
    def search_knowledge_base(self, query):
        connection = DBConnection()
        result = connection.getResult(query)
        if result:
            return result["definition"]
    
    def generate_response(self, query, temp):
        response = self.search_knowledge_base(query)
        if response:
            prompt = "Sử dụng thông tin sau đây để trả lời câu hỏi.\n"
            prompt += f"Dữ liệu: {response}\nCâu hỏi: {query}"
            return self.call_llm_api(prompt, temp)
        else:
            return self.call_llm_api(query, temp)
    
# def main():
#     s = input("Please enter your question: ")
#     chatbot = Chat()
#     print(chatbot.call_llm_api(s, 1))
    
# if __name__ == "__main__":
#     main()