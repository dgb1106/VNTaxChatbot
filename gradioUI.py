import gradio as gr
from chat import Chat
import normalizeQuestion

chatbot = Chat()

def getResponse(question, temperature):
    prompt = normalizeQuestion.preprocess_query(question)
    answer = chatbot.generate_response(prompt, temperature)
    return answer

demo = gr.Interface(
    fn=getResponse,
    inputs=["text", "slider"],
    outputs=["markdown"],
)

demo.launch(share=True)