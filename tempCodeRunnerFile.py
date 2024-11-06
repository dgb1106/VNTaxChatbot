
def main():
    s = input("Please enter your question: ")
    chatbot = Chat()
    print(chatbot.call_llm_api(s))
    
if __name__ == "__main__":
    main()