from TTS.api import TTS
import subprocess
import os
import logging

logger = logging.getLogger(__name__)

def synthesize_speech(input_text: str, user_audio_path:str, output_audio_path: str, language: str):
    """
    Synthesizes speech from text using the specified language.
    """
    model_name = "tts_models/multilingual/multi-dataset/xtts_v2"
    tts = TTS(model_name=model_name, progress_bar=True, gpu=False)
    
    tts.tts_to_file(text=input_text, 
                    language=language, 
                    speaker_wav=user_audio_path,
                    file_path=output_audio_path)
    logger.info(f"Generated audio saved at {output_audio_path}")


