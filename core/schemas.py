from pydantic import BaseModel
from typing import Optional

class VocabResponse(BaseModel):
    sucesso: bool
    mensagem_erro: Optional[str] = None
    palavra_original: Optional[str] = None
    idioma_alvo: Optional[str] = None
    traducao: Optional[str] = None
    frase_exemplo: Optional[str] = None
