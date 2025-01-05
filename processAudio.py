import os
from speechToText import speech_to_text
from translateText import translate_text
from synthesizeSpeech import synthesize_speech

def process_audio(audio_path: str, output_audio_path: str):
    """
    Processes the input audio: detects language, transcribes, translates,
    and generates speech in the target language.
    """
    text, detected_language = speech_to_text(audio_path)
    
    if not text:
        return "Error processing audio"
    
    if detected_language == 'en':
        translated_text = translate_text(text, src_lang='en', dest_lang='hi')
        target_language = 'hi'
    else:  # Assuming Hindi if not English
        translated_text = translate_text(text, src_lang='hi', dest_lang='en')
        target_language = 'en'
    
    synthesize_speech(translated_text, audio_path, output_audio_path, language=target_language)
    
    return text, translated_text
