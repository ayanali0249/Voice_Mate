import pyttsx3
import speech_recognition as sr
import pyautogui
import webbrowser
import os
import datetime

# Initialize pyttsx3 engine for text-to-speech
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speed of speech
engine.setProperty('volume', 1)  # Volume (0.0 to 1.0)

def speak(message):
    """Function to speak out a message"""
    engine.say(message)
    engine.runAndWait()

def listen():
    """Function to listen for user voice commands"""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for a command...")
        recognizer.adjust_for_ambient_noise(source)  # Adjusts for ambient noise
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
            print("Recognizing...")
            command = recognizer.recognize_google(audio).lower()
            print(f"You said: {command}")
            return command
        except sr.UnknownValueError:
            speak("Sorry, I didn't understand that.")
            return None
        except sr.RequestError:
            speak("Sorry, the speech service is unavailable.")
            return None
        except Exception as e:
            speak("An error occurred while listening.")
            print(f"Error: {e}")
            return None

def list_capabilities():
    """List all capabilities of the assistant."""
    capabilities = [
        "Open YouTube using a web browser.",
        "Perform Google searches for a query.",
        "Take a screenshot and save it locally.",
        "Open and control applications like Calculator and Notepad.",
        "Open Google Chrome using the operating system.",
        "Tell the current time and date.",
        "Shut down the system.",
        "Simulate key presses or mouse clicks.",
        "Browse specific websites.",
        "Open any file or folder on your system."
    ]
    speak("Here is a list of things I can do:")
    for capability in capabilities:
        speak(capability)

def execute_command(command):
    """Function to execute actions based on voice commands"""
    if command is None:
        return

    # Web navigation
    if 'open youtube' in command:
        speak("Opening YouTube.")
        webbrowser.open("https://www.youtube.com")
    elif 'search for' in command:
        query = command.replace("search for", "").strip()
        speak(f"Searching for {query}.")
        webbrowser.open(f"https://www.google.com/search?q={query}")
    elif 'open gmail' in command:
        speak("Opening Gmail.")
        webbrowser.open("https://mail.google.com")
    elif 'refresh page' in command:
        speak("Refreshing the current page.")
        pyautogui.hotkey("ctrl", "r")
    
    # Desktop actions
    elif 'take a screenshot' in command:
        speak("Taking a screenshot.")
        screenshot = pyautogui.screenshot()
        file_name = f"screenshot_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.png"
        screenshot.save(file_name)
        speak(f"Screenshot saved as {file_name}.")
    elif 'type' in command:
        text = command.replace("type", "").strip()
        speak(f"Typing: {text}")
        pyautogui.write(text)
    elif 'press enter' in command:
        speak("Pressing Enter.")
        pyautogui.press("enter")
    
    # System-level commands
    elif 'open calculator' in command:
        speak("Opening Calculator.")
        os.system("calc")
    elif 'open notepad' in command:
        speak("Opening Notepad.")
        os.system("notepad")
    elif 'open chrome' in command:
        speak("Opening Google Chrome.")
        os.system("start chrome")
    
    # Time and date
    elif 'what is the time' in command:
        current_time = datetime.datetime.now().strftime("%H:%M")
        speak(f"The current time is {current_time}.")
    elif 'what is the date' in command:
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        speak(f"Today's date is {current_date}.")
    
    # Capabilities
    elif 'what can you do' in command:
        speak("I can assist you with various tasks.")
        list_capabilities()
    
    # System shutdown
    elif 'shutdown' in command:
        speak("Shutting down the system.")
        os.system("shutdown /s /f /t 0")
    elif 'stop' in command or 'exit' in command or 'close' in command:
        speak("Goodbye! I am shutting down.")
        exit()
    else:
        speak("Sorry, I didn't understand that command.")

# Main loop to keep listening for commands
def main():
    speak("Hello, I am your assistant. How can I help you today?")
    while True:
        command = listen()
        if command:
            execute_command(command)

if __name__ == "__main__":
    main()
