import gradio as gr
from chat import Chat
import normalizeQuestion

chatbot = Chat()

def greet(question):
    prompt = normalizeQuestion.preprocess_query(question)
    answer = chatbot.generate_response(prompt)
    return answer

demo = gr.Interface(
    fn=greet,
    inputs=["text"],
    outputs=["text"],
)

demo.launch(share=True)