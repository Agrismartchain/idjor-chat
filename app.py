import gradio as gr
from transformers import pipeline

# Pipeline de test générique
chat = pipeline("text-generation", model="gpt2")

def respond(message, history):
    prompt = "\n".join([f"User: {u}\nBot: {b}" for u, b in history] + [f"User: {message}\nBot:"])
    out = chat(prompt, max_length=100)[0]["generated_text"].split("Bot:")[-1].strip()
    history.append((message, out))
    return history, history

with gr.Blocks() as demo:
    gr.Markdown("# idjor.ai – Prototype Chat FR/Baoulé")
    chatbot = gr.Chatbot()
    txt = gr.Textbox(placeholder="Écris en français ou en Baoulé…", label="Ton message")
    txt.submit(respond, [txt, chatbot], [chatbot, chatbot])
demo.launch()
