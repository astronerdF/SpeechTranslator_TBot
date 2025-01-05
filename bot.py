import os
import logging

from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    CallbackContext,
    filters
)

from processAudio import process_audio

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Telegram Bot Token (replace with your actual token)
TOKEN = "7850275415:AAFXd3SGz6rRkZRl8PNGlGnppgVNkoxaXkc"

# Directory where temporary audio files are stored
TEMP_DIR = "."

async def start(update: Update, context: CallbackContext):
    user_first_name = update.effective_user.first_name
    await update.message.reply_text(
        f"Hi {user_first_name}! 🎙️ Send me a voice message, and I'll send back an audio of the translated version."
    )


async def refresh(update: Update, context: CallbackContext):
    """
    Clears any stored conversation data and deletes leftover audio files.
    """
    # Clear conversation data if you keep any
    context.user_data.clear()
    context.chat_data.clear()

    # Remove leftover .ogg/.wav files in TEMP_DIR
    for filename in os.listdir(TEMP_DIR):
        if filename.endswith(".ogg") or filename.endswith(".wav"):
            file_path = os.path.join(TEMP_DIR, filename)
            try:
                os.remove(file_path)
            except Exception as e:
                logger.warning(f"Could not delete {file_path}: {e}")

    await update.message.reply_text("Conversation refreshed and temporary files removed.")

async def handle_audio(update: Update, context: CallbackContext):
    audio_file = await update.message.voice.get_file()

    # Save audio locally
    audio_path = os.path.join(TEMP_DIR, "input_audio.ogg")
    output_path = os.path.join(TEMP_DIR, "output_audio.wav")
    await audio_file.download_to_drive(audio_path)

    # Process the audio
    original_text, translated_text = process_audio(audio_path, output_path)

    if original_text == "Error processing audio" or not translated_text:
        await update.message.reply_text("Sorry, something went wrong.")
        # Cleanup
        if os.path.exists(audio_path):
            os.remove(audio_path)
        if os.path.exists(output_path):
            os.remove(output_path)
        return

    # Reply with text results
    await update.message.reply_text(f"Original Text: {original_text}")
    await update.message.reply_text(f"Translated Text: {translated_text}")

    # Send the generated audio
    with open(output_path, 'rb') as audio:
        await update.message.reply_voice(voice=audio)

    # Cleanup
    os.remove(audio_path)
    os.remove(output_path)

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("refresh", refresh))

    # For handling voice messages
    app.add_handler(MessageHandler(filters.VOICE, handle_audio))

    app.run_polling()

if __name__ == "__main__":
    main()