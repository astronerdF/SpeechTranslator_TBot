from deep_translator import GoogleTranslator
import logging

logger = logging.getLogger(__name__)

def translate_text(text: str, src_lang: str, dest_lang: str) -> str:
    """
    Translates text from the source language to the destination language using deep-translator.
    """
    try:
        translated_text = GoogleTranslator(source=src_lang, target=dest_lang).translate(text)
        return translated_text
    except Exception as e:
        logger.error(f"Translation Error: {e}")
        return None
