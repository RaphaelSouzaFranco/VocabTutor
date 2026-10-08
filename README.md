# VocabTutor: Multimodal Language Tutor

**VocabTutor** is an interactive language learning agent built in Python that utilizes the multimodal capabilities of **Gemini 1.5 Flash**. The system allows the user to take a photo of an object and provide a voice command stating the target language for translation. It then processes this information to return the original word, the target language, the translation, an example sentence, and the audio pronunciation.

## Technology Stack

- **Language:** Python 3.11+
- **User Interface (UI):** Gradio
- **Multimodal AI:** Google Generative AI (Gemini 1.5 Flash)
- **Text-to-Speech:** gTTS
- **Data Validation:** Pydantic
- **Environment Management:** python-dotenv

## Project Structure

* **`requirements.txt`:** Contains all the project dependencies.
* **`.env`:** File to store your API key (`GEMINI_API_KEY`).
* **`core/config.py`:** Environment variables manager.
* **`core/schemas.py`:** The `VocabResponse` model with strict typing via `pydantic`.
* **`core/agent.py`:** Multimodal communication logic with the Gemini API.
* **`core/tts.py`:** Text-to-audio conversion module using `gTTS`.
* **`main.py`:** Application entry point and UI implemented with Gradio.
* **`assets/`:** Folder for temporary storage of generated audio files.

## How to Run

Follow the steps below to start and test the project locally:

1. **Configure the API Key**
   Open the `.env` file located in the project root and replace the current value with your Google Gemini API key:
   ```env
   GEMINI_API_KEY=your_api_key_here
   ```

2. **Install Dependencies**
   Open the terminal in the project directory and install the necessary libraries by running:
   ```powershell
   pip install -r requirements.txt
   ```

3. **Start the Application**
   In the terminal, run the main entry point:
   ```powershell
   python main.py
   ```
   *After running the command, Gradio will generate a local link (e.g., `http://127.0.0.1:7860/`). Open it in your browser to use VocabTutor.*
