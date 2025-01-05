# **Voice Translator Telegram Bot** 🎙️

This is a Telegram bot that transcribes voice messages, translates them to a different language, and sends back the translated version as an audio message. The bot currently supports translation between **English** and **Hindi**.

---

## **Features**

- Automatically detects the language of the received voice message.
- Translates the message into a different language.
- Sends back a voice message of the translated text.
- Cleans up temporary audio files after processing.

---

## **Setup Instructions**

### **1. Clone the repository**

```python
git clone https://github.com/your-username/voice-translator-bot.git
cd voice-translator-bot
```



### 1. Clone the Repository
```python
git clone https://github.com/your-repo/voice-translator-bot.git
cd voice-translator-bot
```

### 2. Create a Virtual Environment (optional but recommended)
On **Linux/macOS**:
```python
python -m venv venv
source venv/bin/activate
```

On **Windows**:
```python
python -m venv venv
venv\Scripts\activate
```

### 3. Install the Required Dependencies
```python
pip install -r requirements.txt
```

### 4. Set Up Your Telegram Bot Token
Create a `.env` file in the root directory and add your bot token:
```python
TOKEN=your-telegram-bot-token
```
This ensures that your token is kept secure and not directly exposed in your code.

---

## Running the Bot
Once everything is set up, you can start the bot using:
```python
python bot.py
```

---

## Dependencies
Ensure the following are installed before running the bot:
- **Python 3.8+**
- Libraries (installed via `requirements.txt`):
  - `python-telegram-bot`
  - `torch`
  - `whisper`
  - `TTS`
  - `deep-translator`
- **Optional**: CUDA support for faster audio processing if using a GPU.

---

## File Structure
```python
voice-translator-bot/
├── bot.py                  # Main bot logic
├── processAudio.py         # Handles audio processing, transcription, and translation
├── synthesizeSpeech.py     # Generates voice from text using TTS
├── speechToText.py         # Transcribes audio using Whisper
├── translateText.py        # Translates text using Google Translator API
├── requirements.txt        # List of dependencies
├── README.md               # Project documentation
└── .env.example            # Example .env file for storing your bot token
```

---

## Environment Variables
The project uses environment variables for sensitive data like the Telegram Bot token. Create a `.env` file in the root directory and add the following:
```python
TOKEN=your-telegram-bot-token
```

To prevent accidental exposure of your token, make sure to add `.env` to your `.gitignore` file:
```python
.env
```

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Contributions
Contributions are welcome! Feel free to open an issue or submit a pull request.

---

## Acknowledgements
- OpenAI Whisper for speech-to-text.
- Deep Translator for language translation.
- TTS for text-to-speech synthesis.
- python-telegram-bot for the Telegram bot framework.

---

## Author
Your Name – [GitHub Profile](https://github.com/your-profile)