import google.generativeai as genai
import os
import json
from core.config import GEMINI_API_KEY
from core.schemas import VocabResponse
from PIL import Image

import mimetypes

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-3.8-flash')

def process_multimodal_input(image_path: str, audio_path: str) -> VocabResponse:
    try:
        if not GEMINI_API_KEY or GEMINI_API_KEY == "sua_chave_api_aqui":
            return VocabResponse(sucesso=False, mensagem_erro="API Key do Gemini não configurada corretamente no .env")
        
        # Determina o MIME type do áudio
        mime_type, _ = mimetypes.guess_type(audio_path)
        if not mime_type:
            if audio_path.lower().endswith(".wav"):
                mime_type = "audio/wav"
            elif audio_path.lower().endswith(".mp3"):
                mime_type = "audio/mp3"
            elif audio_path.lower().endswith(".ogg"):
                mime_type = "audio/ogg"
            else:
                mime_type = "audio/wav"

        with open(audio_path, "rb") as f:
            audio_bytes = f.read()

        audio_part = {
            "mime_type": mime_type,
            "data": audio_bytes
        }

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
            [prompt, image, audio_part],
            generation_config=genai.types.GenerationConfig(
                response_mime_type="application/json",
            )
        )
        
        data = json.loads(response.text)
        return VocabResponse(**data)
        
    except Exception as e:
        return VocabResponse(sucesso=False, mensagem_erro=str(e))
