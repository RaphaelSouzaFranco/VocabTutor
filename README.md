# 🗣️🖼️ VocabTutor: Multimodal Language Tutor

O **VocabTutor** é um agente interativo de ensino de idiomas desenvolvido em Python que utiliza capacidades multimodais do **Gemini 1.5 Flash**. O sistema permite ao usuário tirar uma foto de um objeto, fornecer um comando de voz informando para qual idioma quer traduzir, e então processa tudo isso para retornar a palavra original, o idioma alvo, a tradução, uma frase de exemplo e a pronúncia em áudio.

## 🛠️ Stack Tecnológica

- **Linguagem:** Python 3.11+
- **Interface UI:** Gradio
- **IA Multimodal:** Google Generative AI (Gemini 1.5 Flash)
- **Text-to-Speech:** gTTS
- **Validação de Dados:** Pydantic
- **Gerenciamento de Env:** python-dotenv

## 📁 Estrutura do Projeto

* **`requirements.txt`:** Contém todas as dependências do projeto.
* **`.env`:** Arquivo para armazenar sua chave da API (`GEMINI_API_KEY`).
* **`core/config.py`:** Gerenciador de variáveis de ambiente.
* **`core/schemas.py`:** O modelo `VocabResponse` com a tipagem estrita via `pydantic`.
* **`core/agent.py`:** Lógica de comunicação multimodal com a API do Gemini.
* **`core/tts.py`:** Módulo de conversão de texto em áudio usando `gTTS`.
* **`main.py`:** Ponto de entrada da aplicação e Interface UI implementada com Gradio.
* **`assets/`:** Pasta para armazenamento temporário de arquivos de áudio gerados.

## 🚀 Como Executar

Siga os passos abaixo para iniciar e testar o projeto localmente:

1. **Configurar a Chave da API**
   Abra o arquivo `.env` localizado na raiz do projeto e substitua o valor atual pela sua chave da API do Google Gemini:
   ```env
   GEMINI_API_KEY=sua_chave_api_aqui
   ```

2. **Instalar Dependências**
   Abra o terminal no diretório do projeto e instale as bibliotecas necessárias executando:
   ```powershell
   pip install -r requirements.txt
   ```

3. **Iniciar a Aplicação**
   No terminal, execute o ponto de entrada principal:
   ```powershell
   python main.py
   ```
   *Após rodar o comando, o Gradio irá gerar um link local (como `http://127.0.0.1:7860/`). Abra-o no seu navegador para utilizar o VocabTutor.*
