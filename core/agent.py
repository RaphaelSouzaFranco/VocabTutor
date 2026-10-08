import google.generativeai as genai
import os
import json
from core.config import GEMINI_API_KEY
from core.schemas import VocabResponse
from PIL import Image

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

def process_multimodal_input(image_path: str, audio_path: str) -> VocabResponse:
    uploaded_audio = None
    try:
        if not GEMINI_API_KEY or GEMINI_API_KEY == "sua_chave_api_aqui":
            return VocabResponse(sucesso=False, mensagem_erro="API Key do Gemini não configurada corretamente no .env")
        
        uploaded_audio = genai.upload_file(path=audio_path)
        image = Image.open(image_path)
        
        prompt = """
        Extraia o idioma desejado a partir do áudio, identifique o objeto central da imagem e retorne o JSON no formato exato solicitado.
        O áudio contém um comando informando para qual idioma a palavra deve ser traduzida.
        A imagem contém o objeto a ser identificado.
        Retorne um JSON estrito validado pelo Pydantic, contendo: `palavra_original`, `idioma_alvo`, `traducao` e `frase_exemplo`.
        Exemplo de formato:
        {
            "sucesso": true,
            "palavra_original": "maçã",
            "idioma_alvo": "inglês",
            "traducao": "apple",
            "frase_exemplo": "I eat an apple every day."
        }
        """
        
        response = model.generate_content(
            [prompt, image, uploaded_audio],
            generation_config=genai.types.GenerationConfig(
                response_mime_type="application/json",
            )
        )
        
        data = json.loads(response.text)
        return VocabResponse(**data)
        
    except Exception as e:
        return VocabResponse(sucesso=False, mensagem_erro=str(e))
    finally:
        if uploaded_audio:
            try:
                genai.delete_file(uploaded_audio.name)
            except:
                pass
