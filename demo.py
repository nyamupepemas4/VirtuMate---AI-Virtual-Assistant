import pyautogui
import time
import json
import pyttsx3
import tkinter as tk
from tkinter import messagebox

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    """Speak the given text."""
    engine.say(text)
    engine.runAndWait()

# Load saved tasks
TASK_FILE = "tasks.json"

def load_tasks():
    try:
        with open(TASK_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

saved_tasks = load_tasks()

def show_instruction(step):
    """Display on-screen instructions."""
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Step-by-Step Guide", step)

def execute_task(task_name):
    """Execute a predefined or saved task."""
    tasks = load_tasks()
    if task_name in tasks:
        steps = tasks[task_name]
        for step in steps:
            speak(step["instruction"])
            show_instruction(step["instruction"])
            if step["action"] == "click":
                pyautogui.click(step["x"], step["y"])
            elif step["action"] == "type":
                pyautogui.typewrite(step["text"], interval=0.1)
            elif step["action"] == "wait":
                time.sleep(step["duration"])
        speak("Task completed.")
    else:
        speak("I don't know how to do that yet. Would you like to teach me?")

def learn_task(task_name):
    """Learn a new task from the user."""
    steps = []
    speak("Let's start recording the steps. Say 'done' when finished.")
    while True:
        instruction = input("Enter instruction: ")
        if instruction.lower() == "done":
            break
        action = input("Action (click/type/wait): ")
        step = {"instruction": instruction, "action": action}
        if action == "click":
            x, y = pyautogui.position()
            step.update({"x": x, "y": y})
        elif action == "type":
            text = input("Enter text to type: ")
            step.update({"text": text})
        elif action == "wait":
            duration = int(input("Enter wait time (seconds): "))
            step.update({"duration": duration})
        steps.append(step)
    saved_tasks[task_name] = steps
    save_tasks(saved_tasks)
    speak("Task saved successfully.")

# Example predefined task
def predefined_tasks():
    return {
        "open_notepad": [
            {"instruction": "Opening Notepad", "action": "click", "x": 100, "y": 100},
            {"instruction": "Typing 'Hello, this is VirtuMate'", "action": "type", "text": "Hello, this is VirtuMate"},
            {"instruction": "Task completed", "action": "wait", "duration": 1}
        ]
    }

saved_tasks.update(predefined_tasks())
save_tasks(saved_tasks)

# Example usage:
# execute_task("open_notepad")  # Runs a predefined task
# learn_task("search_google")  # Learns a new task
