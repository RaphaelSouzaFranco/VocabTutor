from gtts import gTTS
import tempfile
import os

def generate_tts(text: str, lang: str) -> str:
    """
    Converte texto em áudio usando gTTS.
    lang deve ser o código ISO (ex: 'en', 'es', 'pt', etc.) ou nome do idioma.
    Retorna o caminho do arquivo gerado temporariamente.
    """
    try:
        # Mapeamento simples de nome de idioma para código ISO
        lang_map = {
            "inglês": "en",
            "ingles": "en",
            "english": "en",
            "espanhol": "es",
            "spanish": "es",
            "francês": "fr",
            "frances": "fr",
            "french": "fr",
            "alemão": "de",
            "alemao": "de",
            "german": "de",
            "italiano": "it",
            "italian": "it",
            "português": "pt",
            "portugues": "pt",
            "japonês": "ja",
            "japones": "ja",
            "japanese": "ja"
        }
        
        iso_lang = lang_map.get(lang.lower().strip(), "en")
        
        tts = gTTS(text=text, lang=iso_lang, slow=False)
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.mp3', dir=os.path.join(os.getcwd(), 'assets'))
        temp_path = temp_file.name
        temp_file.close()
        
        tts.save(temp_path)
        return temp_path
    except Exception as e:
        print(f"Erro no TTS: {e}")
        return None
