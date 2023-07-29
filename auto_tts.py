from flask import Flask, render_template, request, jsonify
from googletrans import Translator
from gtts import gTTS
from langdetect import detect
import requests
import os

app = Flask(__name__)

# Homepage
@app.route("/")
def index():
    return render_template("index.html")

# Endpoint for handling speech input and translation
@app.route("/translate", methods=["POST"])
def translate():
    try:
        # Receive speech input from the frontend
        speech_data = request.form.get("speech")

        # Detect user's language using language detection library (langdetect)
        user_language_code = detect_user_language(speech_data)

        # Translate the speech
        translated_text = translate_speech(speech_data, user_language_code)

        # Convert the translated text to audio
        translated_audio = generate_audio(translated_text, user_language_code)

        # Return the translated text and audio to the frontend
        return jsonify({"translated_text": translated_text, "translated_audio": translated_audio})

    except Exception as e:
        return jsonify({"error": str(e)})

def detect_user_language(speech_data):
    # Use language detection library to automatically detect the user's language
    return detect(speech_data)

def translate_speech(speech_data, target_language_code):
    # Use the googletrans library to translate the speech
    translator = Translator()
    translated = translator.translate(speech_data, dest=target_language_code)
    return translated.text

def generate_audio(text, language_code):
    # Use the gTTS library to generate audio
    tts = gTTS(text, lang=language_code, slow=False)
    # Save the audio to a temporary file
    audio_file = "translated_audio.mp3"
    tts.save(audio_file)
    return audio_file

if __name__ == "__main__":
    app.run(debug=True)
