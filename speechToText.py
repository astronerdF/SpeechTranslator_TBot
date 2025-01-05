import whisper
import torch
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize Whisper model
device = "cuda" if torch.cuda.is_available() else "cpu"
whisper_model = whisper.load_model("small")

def speech_to_text(audio_path: str) -> (str, str):
    """
    Converts speech to text and detects language of the audio.
    If detected language is not English ('en'), treat it as Hindi ('hi').
    Returns the transcribed text and "en" or "hi" only.
    """
    try:
        result = whisper_model.transcribe(audio_path)
        detected_language = result['language']
        text = result['text']
        logger.info(f"Detected Language: {detected_language}")

        # If it's not English, override to Hindi
        if detected_language != "en":
            detected_language = "hi"

        return text, detected_language
    except Exception as e:
        logger.error(f"Speech-to-Text Error: {e}")
        return None, None
