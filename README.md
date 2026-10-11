# VocabTutor: Multimodal Language Tutor

[English Version](#english-version) | [Versão em Português](#versão-em-português)

---

## English Version

**VocabTutor** is an interactive language learning agent built in Python that utilizes the multimodal capabilities of **Gemini 1.5 Flash**. The system allows the user to take a photo of an object and provide a voice command stating the target language for translation. It then processes this information to return the original word, the target language, the translation, an example sentence, and the audio pronunciation.

### Technology Stack

- **Language:** Python 3.11+
- **User Interface (UI):** Gradio
- **Multimodal AI:** Google Generative AI (Gemini 1.5 Flash)
- **Text-to-Speech:** gTTS
- **Data Validation:** Pydantic
- **Environment Management:** python-dotenv
- **Containerization:** Docker

### Project Structure

* **`requirements.txt`:** Contains all the project dependencies.
* **`.env.example`:** Template file for environment variables.
* **`Dockerfile`:** Instructions to build the Docker image.
* **`.dockerignore`:** Specifies files to be ignored by Docker during the build process (e.g., `.env`).
* **`core/config.py`:** Environment variables manager.
* **`core/schemas.py`:** The `VocabResponse` model with strict typing via `pydantic`.
* **`core/agent.py`:** Multimodal communication logic with the Gemini API.
* **`core/tts.py`:** Text-to-audio conversion module using `gTTS`.
* **`main.py`:** Application entry point and UI implemented with Gradio.
* **`assets/`:** Folder for temporary storage of generated audio files.

### How to Run

You can run this project via **Docker** (recommended for review) or locally with **Python**.

#### Option A: Running via Docker (Recommended)

Running via Docker ensures the application executes in an isolated, standardized environment.

1. **Configure the API Key**  
   Duplicate the `.env.example` file, rename the copy to `.env`, and insert your Google Gemini API key:
   ```env
   GEMINI_API_KEY=your_api_key_here
   ```

2. **Build the Docker Image**  
   Open the terminal in the project directory and build the image:
   ```bash
   docker build -t vocabtutor .
   ```

3. **Run the Container**  
   Start the container, mapping the port and injecting the environment variables:
   ```bash
   docker run -p 7860:7860 --env-file .env vocabtutor
   ```

4. **Access the Application**  
   Open your browser and navigate to: [http://localhost:7860](http://localhost:7860)

#### Option B: Running Locally (Python)

1. **Configure the API Key**  
   Duplicate `.env.example`, rename it to `.env`, and add your API key.

2. **Install Dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

3. **Start the Application**  
   ```bash
   python main.py
   ```

   After running the command, open the local link provided in the terminal (e.g., [http://127.0.0.1:7860/](http://127.0.0.1:7860/)) in your browser.

---

## Versão em Português

O **VocabTutor** é um agente interativo de ensino de idiomas desenvolvido em Python que utiliza capacidades multimodais do **Gemini 1.5 Flash**. O sistema permite ao usuário tirar uma foto de um objeto, fornecer um comando de voz informando para qual idioma quer traduzir, e então processa tudo isso para retornar a palavra original, o idioma alvo, a tradução, uma frase de exemplo e a pronúncia em áudio.

### Stack Tecnológica

- **Linguagem:** Python 3.11+
- **Interface UI:** Gradio
- **IA Multimodal:** Google Generative AI (Gemini 1.5 Flash)
- **Text-to-Speech:** gTTS
- **Validação de Dados:** Pydantic
- **Gerenciamento de Env:** python-dotenv
- **Containerização:** Docker

### Estrutura do Projeto

* **`requirements.txt`:** Contém todas as dependências do projeto.
* **`.env.example`:** Arquivo de modelo para as variáveis de ambiente.
* **`Dockerfile`:** Instruções para a construção da imagem Docker.
* **`.dockerignore`:** Especifica arquivos que devem ser ignorados pelo Docker durante o build (ex: `.env`).
* **`core/config.py`:** Gerenciador de variáveis de ambiente.
* **`core/schemas.py`:** O modelo `VocabResponse` com a tipagem estrita via `pydantic`.
* **`core/agent.py`:** Lógica de comunicação multimodal com a API do Gemini.
* **`core/tts.py`:** Módulo de conversão de texto em áudio usando `gTTS`.
* **`main.py`:** Ponto de entrada da aplicação e Interface UI implementada com Gradio.
* **`assets/`:** Pasta para armazenamento temporário de arquivos de áudio gerados.

### Como Executar

Você pode rodar este projeto via **Docker** (recomendado para avaliação) ou localmente com **Python**.

#### Opção A: Rodando via Docker (Recomendado)

Rodar via Docker garante que a aplicação seja executada em um ambiente isolado e padronizado.

1. **Configurar a Chave da API**  
   Duplique o arquivo `.env.example`, renomeie a cópia para `.env` e insira a sua chave da API do Google Gemini:
   ```env
   GEMINI_API_KEY=sua_chave_api_aqui
   ```

2. **Construir a Imagem Docker**  
   Abra o terminal no diretório do projeto e construa a imagem:
   ```bash
   docker build -t vocabtutor .
   ```

3. **Rodar o Container**  
   Inicie o container mapeando a porta e injetando as variáveis de ambiente:
   ```bash
   docker run -p 7860:7860 --env-file .env vocabtutor
   ```

4. **Acessar a Aplicação**  
   Abra o seu navegador e acesse: [http://localhost:7860](http://localhost:7860)

#### Opção B: Rodando Localmente (Python)

1. **Configurar a Chave da API**  
   Duplique o `.env.example`, renomeie para `.env` e adicione sua chave da API.

2. **Instalar Dependências**  
   ```bash
   pip install -r requirements.txt
   ```

3. **Iniciar a Aplicação**  
   ```bash
   python main.py
   ```

   Após rodar o comando, abra o link local fornecido no terminal (como [http://127.0.0.1:7860/](http://127.0.0.1:7860/)) no seu navegador.