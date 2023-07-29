# AI-Auto-Translator Web App


## Overview

This is a web app built with Flask that allows users to input speech, automatically detects the language spoken, translates it to the user's preferred language (detected based on location or manually selected), and provides both the translated text and audio playback of the translation.

## Features

- Automatic language detection using the `langdetect` library.
- Translation of speech using the `googletrans` library.
- Text-to-Speech (TTS) conversion for translated text using the `gtts` library.
- User-friendly interface with mic and speaker icons for speech input and audio playback.
- Supports a wide range of languages for translation.

## Requirements

- Python 3.0+
- Flask
- googletrans==4.0.0-rc1
- gtts
- langdetect
- requests

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/pratyush1223/AI-Auto-Translator.git
2. Change into the project directory:
   
   ```bash
   cd AI-Auto-Translator
3. Install the required libraries:

   ```bash
   pip install -r requirements.txt

## Usage

1. Run the Flask app:

   ```bash
   python app.py

1. Access the web app in your browser by visiting http://127.0.0.1:5000/.
2. Use the "Speak something..." textarea to input speech. You can either type or click the microphone icon to start recording your speech.
3. After speaking, click the "Translate" button to get the translated text and play the translated audio using the speaker icon.

## Known Issues / Limitations

 1. Automatic language detection using the langdetect library might not be perfect and could sometimes produce inaccurate results, especially for short or 
    ambiguous inputs.

## Contributing
 1. Contributions are welcome! Feel free to open an issue or submit a pull request for any improvements or bug fixes.

