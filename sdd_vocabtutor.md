# Software Design Document (SDD): Tutor de Vocabulário Multimodal (VocabTutor)

Este documento define a arquitetura, o fluxo de dados e as restrições de engenharia para o desenvolvimento do agente interativo de ensino de idiomas. Ele foi projetado para instruir o assistente de código (Antigravity) a gerar uma aplicação modular, utilizando as capacidades multimodais modernas onde um único modelo processa áudio e imagem simultaneamente.

## 1. Visão Geral do Projeto
*   **Nome:** VocabTutor
*   **Objetivo:** Um agente interativo que recebe uma imagem do ambiente do usuário e um comando de voz, identifica o objeto, traduz para o idioma solicitado e retorna a pronúncia em áudio junto com uma frase de exemplo.
*   **Padrão de Arquitetura:** Pipeline Assíncrono com Interface Reativa (Gradio) e Processamento Multimodal Unificado.

## 2. Stack Tecnológica

| Componente | Tecnologia | Justificativa |
|---|---|---|
| **Linguagem** | Python 3.11+ | Suporte nativo e bibliotecas atualizadas para IA. |
| **Interface (UI)** | `gradio` | Fornece componentes prontos para captura de microfone e câmera/upload de imagem via web. |
| **Cérebro Multimodal**| `google-generativeai` | O modelo **Gemini 1.5 Flash** processa o arquivo de áudio e a imagem em uma única chamada de forma eficiente. |
| **Geração de Áudio (TTS)**| `gTTS` ou `openai` | `gTTS` é gratuito para MVP; API da OpenAI oferece vozes mais naturais para ambiente de produção. |
| **Validação de Dados** | `pydantic` | Garante que o LLM retorne a palavra, tradução e frase em formato JSON estrito. |
| **Gerenciamento** | `python-dotenv` | Carregamento seguro das chaves de configuração e API (`GEMINI_API_KEY`). |

## 3. Estrutura de Diretórios Recomendada

```text
vocab-tutor/
├── .env                 # Chaves de API (ignorado no git)
├── requirements.txt     # Dependências (gradio, google-generativeai, gTTS, pydantic)
├── main.py              # Ponto de entrada (Interface Gradio)
├── core/
│   ├── __init__.py
│   ├── config.py        # Carregamento de variáveis de ambiente
│   ├── schemas.py       # Pydantic models (VocabResponse)
│   ├── agent.py         # Lógica de comunicação com o Gemini (Áudio + Imagem)
│   └── tts.py           # Módulo para converter texto em áudio
└── assets/              # Arquivos de áudio temporários gerados
```

## 4. Fluxo de Dados (Data Flow)

1.  **Captura (Gradio):** O usuário faz o upload/tira uma foto e grava um áudio no microfone. O sistema salva os dados temporariamente no disco.
2.  **Upload Multimodal:** O arquivo de áudio e a imagem são enviados para a API do Gemini via `genai.upload_file()`.
3.  **Inferência Unificada:** O arquivo `agent.py` envia a mídia e o prompt de sistema para o modelo cruzar o comando de áudio com o contexto visual da imagem.
4.  **Validação:** A resposta retorna em JSON estrito validado pelo Pydantic, contendo: `palavra_original`, `idioma_alvo`, `traducao` e `frase_exemplo`.
5.  **Síntese de Voz (TTS):** O arquivo `tts.py` recebe o texto traduzido e a frase de exemplo, detecta o idioma alvo e gera um arquivo `.mp3` correspondente.
6.  **Retorno (UI):** O Gradio exibe os textos extraídos e reproduz o áudio gerado automaticamente na interface para o usuário.

## 5. Diretrizes e Melhores Práticas para o Antigravity

*   **Gerenciamento de Arquivos do Gemini:** Faça o upload do áudio via `genai.upload_file()` antes da chamada de geração e implemente a exclusão do arquivo na API do Google após a inferência para não consumir cota de armazenamento desnecessária.
*   **Prompt de Sistema:** Seja explícito nas instruções dentro do `agent.py`: *"Extraia o idioma desejado a partir do áudio, identifique o objeto central da imagem e retorne o JSON no formato exato solicitado."*
*   **Manipulação de Áudio no Gradio:** Utilize o componente `gr.Audio(type="filepath")` para capturar e passar adiante o caminho do arquivo temporário salvo no disco, facilitando o upload posterior para APIs externas.
*   **Isolamento do TTS:** A função de Text-to-Speech deve ser completamente agnóstica (aceitar apenas a string de texto e o código ISO do idioma como parâmetros) e salvar o áudio localmente usando o módulo `tempfile` nativo do Python para evitar concorrência e sobrescrita entre usuários diferentes.
*   **Tratamento de Exceções e Edge Cases:** Modele o schema JSON de saída (`schemas.py`) para suportar falhas de identificação (ex: adicionar campos `sucesso: boolean` e `mensagem_erro: str`), permitindo que a interface informe o usuário caso a foto seja muito escura ou o áudio ininteligível, sem quebrar a execução do programa.