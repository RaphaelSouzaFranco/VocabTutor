import gradio as gr
from core.agent import process_multimodal_input
from core.tts import generate_tts

def handle_request(image_path, audio_path):
    if not image_path or not audio_path:
        return "Por favor, forneça a imagem e grave o áudio.", None
        
    response = process_multimodal_input(image_path, audio_path)
    
    if not response.sucesso:
        return f"Erro: {response.mensagem_erro}", None
        
    resultado_texto = f"**Palavra Original:** {response.palavra_original}\n\n"
    resultado_texto += f"**Idioma Alvo:** {response.idioma_alvo}\n\n"
    resultado_texto += f"**Tradução:** {response.traducao}\n\n"
    resultado_texto += f"**Frase de Exemplo:** {response.frase_exemplo}\n"
    
    texto_para_falar = f"{response.traducao}. {response.frase_exemplo}"
    audio_resultado = generate_tts(texto_para_falar, response.idioma_alvo)
    
    return resultado_texto, audio_resultado

with gr.Blocks(title="VocabTutor", theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 🗣️🖼️ VocabTutor: Multimodal Language Tutor")
    gr.Markdown("Tire uma foto de um objeto e fale o idioma para o qual deseja traduzir (ex: 'Como eu digo isso em inglês?').")
    
    with gr.Row():
        with gr.Column():
            image_input = gr.Image(type="filepath", label="Tire a foto ou faça o upload")
            audio_input = gr.Audio(type="filepath", label="Comando de voz (ex: 'traduz para espanhol')")
            submit_btn = gr.Button("Analisar", variant="primary")
            
        with gr.Column():
            text_output = gr.Markdown(label="Resultado")
            audio_output = gr.Audio(label="Pronúncia", interactive=False)
            
    submit_btn.click(
        fn=handle_request,
        inputs=[image_input, audio_input],
        outputs=[text_output, audio_output]
    )

if __name__ == "__main__":
    demo.launch()
