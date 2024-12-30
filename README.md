# Voice Assistant - Python Project

## Overview
This project is a simple **Voice Assistant** built using Python. The assistant can listen to voice commands, recognize them, and execute tasks such as web browsing, taking screenshots, opening applications, and more. The assistant uses the `pyttsx3` library for text-to-speech, `speech_recognition` for speech-to-text, and `pyautogui` for simulating keyboard and mouse actions.

## Features
- **Web Navigation**: Open YouTube, perform Google searches, and open Gmail.
- **Desktop Actions**: Take screenshots, simulate typing, press Enter, and control applications like Calculator and Notepad.
- **System Control**: Open Chrome, refresh the page, and shut down the system.
- **Time and Date**: Get the current time and date.
- **Custom Commands**: Easily extendable for additional commands and functionalities.

## Installation
To run this project, you need Python 3.x installed. Follow the steps below to get started:

### 1. Clone the Repository
Clone the repository to your local machine:

```bash
git clone https://github.com/ayanali0249/voice-assistant-python.git
```

### 2. Install Dependencies
Navigate to the project folder and install the required libraries using `pip`:

```bash
cd voice-assistant-python
pip install -r requirements.txt
```

### 3. Running the Assistant
To start the assistant, simply run the following command:

```bash
python assistant.py
```

The assistant will start listening for voice commands. You can give commands like "open YouTube", "search for Python", or "take a screenshot".

## Usage
Once the assistant is running, you can speak the following commands:

- **Web Navigation**:
  - "open youtube"
  - "search for [query]"
  - "open gmail"
  - "refresh page"

- **Desktop Actions**:
  - "take a screenshot"
  - "type [text]"
  - "press enter"

- **System Control**:
  - "open calculator"
  - "open notepad"
  - "open chrome"
  - "shutdown"

- **Time and Date**:
  - "what is the time"
  - "what is the date"

- **General Commands**:
  - "what can you do"
  - "stop" or "exit" to close the assistant

## Libraries Used
- `pyttsx3` - Text-to-speech conversion.
- `speech_recognition` - Speech-to-text conversion.
- `pyautogui` - Simulating keyboard and mouse actions.
- `webbrowser` - Opening web pages in the browser.
- `os` - Operating system commands.
- `datetime` - Time and date functions.
  
## Demo Video
Here’s a demonstration of how the Voice Assistant works:
https://www.linkedin.com/posts/ayan-ali0249_python-voiceassistant-artificialintelligence-activity-7276542624465874944-qxyG?utm_source=share&utm_medium=member_android

## Contributing
Feel free to fork this project, make changes, and create a pull request. Contributions are always welcome!

