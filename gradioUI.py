import gradio as gr
from chat import Chat

chatbot = Chat()

def greet(question):
    answer = chatbot.call_llm_api(question)
    return answer

demo = gr.Interface(
    fn=greet,
    inputs=["text"],
    outputs=["text"],
)

demo.launch(share=True)