# AI-Auto-Translato Web App


## Overview

This is a web app built with Flask that allows users to input speech, automatically detects the language spoken, translates it to the user's preferred language (detected based on location or manually selected), and provides both the translated text and audio playback of the translation.

## Features

- Automatic language detection using the `langdetect` library.
- Translation of speech using the `googletrans` library.
- Text-to-Speech (TTS) conversion for translated text using the `gtts` library.
- User-friendly interface with mic and speaker icons for speech input and audio playback.
- Supports a wide range of languages for translation.

## Requirements

- Python 3.x
- Flask
- googletrans==4.0.0-rc1
- gtts
- langdetect
- requests

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/speech-translation-web-app.git
