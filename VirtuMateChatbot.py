import requests
import json
import os
import time
import pyttsx3
import re
import speech_recognition as sr

# File to store chat history
CHAT_FILE = "chat_history.json"

# Function to load chat history
def load_chat():
    if os.path.exists(CHAT_FILE):
        with open(CHAT_FILE, "r") as file:
            data = json.load(file)
            # Remove old chats (older than 5 days)
            current_time = time.time()
            data = [chat for chat in data if current_time - chat["timestamp"] <= 432000]
            return data
    return []

# Function to save chat history
def save_chat(user_input, bot_response):
    chat_history = load_chat()
    chat_history.append({"user": user_input, "bot": bot_response, "timestamp": time.time()})
    with open(CHAT_FILE, "w") as file:
        json.dump(chat_history, file, indent=4)

# Function to delete chat history
def delete_chat():
    if os.path.exists(CHAT_FILE):
        os.remove(CHAT_FILE)
        return "Chat history deleted."
    return "No chat history to delete."

# Text-to-speech setup
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 175)

def speak(text):
    engine.say(text)
    engine.runAndWait()

# OpenRouter API settings
API_KEY = "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"
URL = "https://openrouter.ai/api/v1/chat/completions"
HEADERS = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}

# Voice input function
def take_voice_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        try:
            audio = recognizer.listen(source, timeout=5)
            print("Recognizing...")
            return recognizer.recognize_google(audio, language='en-US')
        except sr.UnknownValueError:
            return ""
        except sr.RequestError:
            return "Error: Could not process the voice input."

# Function to handle user input (text or voice)
def chatbot_input(user_input=None):
    if user_input is None:  # If no text input, try voice input
        user_input = take_voice_input()
    
    if user_input.lower() == "delete chat":
        return delete_chat()
    else:
        DATA = {"model": "deepseek/deepseek-r1-zero:free", "messages": [{"role": "user", "content": user_input}]}
        response = requests.post(URL, headers=HEADERS, data=json.dumps(DATA))
        if response.status_code == 200:
            response_json = response.json()
            if "choices" in response_json and response_json["choices"]:
                ai_response = response_json["choices"][0]["message"]["content"].strip()
                ai_response = re.sub(r"\\[a-zA-Z]+{([^}]*)}", r"\1", ai_response)  # Remove LaTeX-style formatting
                save_chat(user_input, ai_response)
                speak(ai_response)  # Speak the response
                return ai_response
            else:
                return "No valid response from AI."
        else:
            return f"Error: {response.status_code} {response.text}"
