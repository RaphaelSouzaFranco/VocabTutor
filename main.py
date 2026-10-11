import gradio as gr
from core.agent import process_multimodal_input
from core.tts import generate_tts

INITIAL_OUTPUT_TEXT = """### 💡 Aguardando envio
Selecione ou tire uma foto ao lado, grave sua dúvida por voz (ex: *"Como se diz isso em inglês?"*) e clique em **Analisar** para ver o resultado aqui!
"""

def handle_request(image_path, audio_path):
    if not image_path and not audio_path:
        return "⚠️ **Atenção:** Por favor, forneça tanto uma imagem quanto uma gravação de áudio.", None
    if not image_path:
        return "⚠️ **Atenção:** Por favor, forneça a imagem do objeto a ser traduzido.", None
    if not audio_path:
        return "⚠️ **Atenção:** Por favor, grave um comando de voz informando o idioma de destino.", None
        
    response = process_multimodal_input(image_path, audio_path)
    
    if not response.sucesso:
        return f"❌ **Erro no processamento:** {response.mensagem_erro}", None
        
    resultado_texto = f"""### ✅ Tradução Identificada

- **Objeto Identificado:** `{response.palavra_original}`
- **Idioma Alvo:** `{response.idioma_alvo}`
- **Tradução:** **{response.traducao}**

---
#### 📖 Frase de Exemplo:
> *"{response.frase_exemplo}"*
"""
    
    texto_para_falar = f"{response.traducao}. {response.frase_exemplo}"
    audio_resultado = generate_tts(texto_para_falar, response.idioma_alvo)
    
    return resultado_texto, audio_resultado

def clear_inputs():
    return None, None, INITIAL_OUTPUT_TEXT, None

with gr.Blocks(title="VocabTutor - Tutor de Idiomas Multimodal") as demo:
    gr.Markdown(
        """
        # 🎓 VocabTutor
        ### Seu tutor inteligente de vocabulário multimodal
        Aprenda como falar qualquer objeto do seu dia a dia em outros idiomas usando fotos e sua voz!
        
        ---
        **Como funciona:**
        1. 📸 **Envie uma foto** ou tire uma foto de um objeto com a câmera.
        2. 🎙️ **Grave um áudio** dizendo para qual idioma deseja traduzir (ex: *"Como se diz em espanhol?"*, *"Traduz para alemão"*).
        3. 🔍 Clique em **Analisar** para ver o nome, a pronúncia e uma frase de exemplo.
        """
    )
    
    with gr.Row():
        with gr.Column(scale=1):
            image_input = gr.Image(type="filepath", label="1. Foto do Objeto", sources=["upload", "webcam"])
            audio_input = gr.Audio(type="filepath", label="2. Comando de Voz (fale o idioma)", sources=["microphone", "upload"])
            with gr.Row():
                submit_btn = gr.Button("🔍 Analisar", variant="primary", scale=2)
                clear_btn = gr.Button("🗑️ Limpar", variant="secondary", scale=1)
            
        with gr.Column(scale=1):
            text_output = gr.Markdown(value=INITIAL_OUTPUT_TEXT, label="Resultado")
            audio_output = gr.Audio(label="🔊 Pronúncia em Áudio", interactive=False)
            
    submit_btn.click(
        fn=handle_request,
        inputs=[image_input, audio_input],
        outputs=[text_output, audio_output]
    )
    
    clear_btn.click(
        fn=clear_inputs,
        inputs=[],
        outputs=[image_input, audio_input, text_output, audio_output]
    )

if __name__ == "__main__":
    demo.launch(theme=gr.themes.Soft())

