import pyautogui
from sqlite3 import Date
from typing_extensions import Self
from numpy import place
import speedtest
import importlib
from jmespath import search
import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import keyboard
import webbrowser
import threading
import pywhatkit
import pyjokes
import os
import wolframalpha
from requests import get, request
import sys
import requests
import pyaudio
from bs4 import BeautifulSoup
from plyer import notification
from playsound import playsound
from pygame import mixer
from pywikihow import search_wikihow
from custom_keyboard import volumeup, volumedown
from keyboard import press_and_release
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from jarvisUi import Ui_jarvisUi
from VirtuMateChatbot import chatbot_input
import psutil
import time
import json
import tkinter as tk
from tkinter import messagebox

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate',175)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def startup():
    
    speak("Checking the internet connection")
    """speak("Wait a moment")
    speak('Updating the cloud configuration')
    speak("All drivers are up and running")
    speak("All systems have been activated")"""

def computational_intelligence(question):
    try:
        client = wolframalpha.Client('4H2PW2-3JYYGVHJQ6')
        answer = client.query(question)
        answer = next(answer.results).text
        print(answer)
        return answer
    except:
        speak("Sorry! I couldn't fetch your question's answer. Please try again")
        return None

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        
        speak("GoodMorning!")

    elif hour>=12 and hour<18:
        speak("GoodAfternoon!")
          

    else:
        speak("GoodEvening!")  
        

    speak("How may I help you")       

class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        self.TaskExecution()


    def takeCommand(self):

        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1                                           
            audio = r.listen(source,0,4)                                                                    

        try:                                                                    
            print("Recognizing...")    
            self.query = r.recognize_google(audio, language='en-us')
            print(f"User said: {self.query}\n")

        except Exception as e:
            # print(e)    
            print("Say that again please...")

            return "None"
        return self.query
    

    def TaskExecution(self):
        startup()
        wishMe()
        while True:
            self.query = self.takeCommand().lower()

           
            if 'go to sleep' in self.query:
                speak("Going to sleep.")
                exit()

#chatbot
            elif self.query in ["let's chat", "can we talk"]:
                speak("Activating the chatbot. Please wait...")
                #chatbot_trigger()

#Temperature
            elif 'current temperature' in self.query:
                search = "temperature in my current location"
                url = f"https://www.google.com/search?q={search}"
                r = requests.get(url)
                data = BeautifulSoup(r.text, "html.parser")
                temp = data.find("div",class_="BNeawe").text
                speak(f'the current temperature in your current location is {temp}')                

            elif 'tell me about' in self.query:
                speak('Searching Wikipedia...please wait')
                
                self.query = self.query.replace("wikipedia", "")
                results =  wikipedia.summary(self.query, sentences = 2)
                speak("Internet says...")
                print(results)
                speak(results) 


            elif "calculate" in self.query:
                question = self.query
                answer = computational_intelligence(question)
                speak(answer)
            
            elif "what is" in self.query or "who is" in self.query:
                question = self.query
                answer = computational_intelligence(question)
                speak(answer)

#Alarm
            elif "set an alarm" in self.query:
                print("input time example:- 10 and 10 and 10")
                speak("Set the time")
                a = input("Please tell the time :- ")
                #alarm(a)
                speak("Done,sir")


#Conversation                
            elif "hello" in self.query:            
                speak("Hello , how are you ?")
            elif "i am fine" in self.query:
                speak("that's great.")
            elif "how are you" in self.query:
                speak("Perfect.")
            elif "thank you" in self.query:
                speak("you are welcome")
            elif "who are you" in self.query:
                speak('My name is VirtuMate. I am an artificial assistant made by Samuel, a sixth simester BCA student. My purpose is to make your work easier by allowing me to help you. You can command me to perform various tasks such as calculating sums or opening applications etcetra')
                
#Time
            elif "time" in self.query:
                strTime = datetime.datetime.now().strftime("%H:%M")    
                speak(f"The time is {strTime}")
            elif "tell me the time" in self.query:
                strTime = datetime.datetime.now().strftime("%H:%M")    
                speak(f"The time is {strTime}")
                
#Music
            elif 'play' in self.query:
                speak('Surfing the browser.... Hold on for a moment') 
                
                # Clean up the query
                cleaned_query = self.query.replace('virtumate', '').replace('play', '').strip()
                
                if cleaned_query:
                    try:
                        from pytube import Search
                        search = Search(cleaned_query)
                        if search.results:
                            video = search.results[0]
                            autoplay_url = f"{video.watch_url}&autoplay=1"
                            webbrowser.open(autoplay_url)
                            speak('Enjoy the music!')
                        else:
                            speak("Sorry, I couldn't find any videos for that query.")
                    except Exception as e:
                        speak("An error occurred while trying to play the video.")
                        print(f"Error: {e}")
                else:
                    speak("Please specify what you want me to play.")
                    
#Game
            elif "game" in self.query:
                from game import game_play
                game_play()

#Jokes
            elif 'tell me a joke' in self.query:
                speak(pyjokes.get_joke())
                
#My IP Address
            elif "ip address" in self.query:
                ip = get("https://api.ipify.org").text
                speak(f'Your current ip address is {ip}') 
                
#Remember
            elif "remember that" in self.query:
                rememberMessage = self.query.replace("remember that","").replace("virtumate","")
                speak("You told me to remember"+ rememberMessage)
                with open("Remember.txt","a") as remember:
                    remember.write(rememberMessage + "\n")  
            elif "what do you remember" in self.query:
                with open("Remember.txt","r") as remember:
                    memories = remember.read()
                    speak("You told me to " + memories if memories else "I don't remember anything yet")
            elif "forget everything" in self.query or "clear memory" in self.query:
                open("Remember.txt", "w").close()  
                speak("All memories have been wiped clean. I remember nothing now.")

#IPL Score
            elif "ipl score" in self.query:
                try:
                    
                    url = "https://www.cricbuzz.com/"
                    page = requests.get(url)
                    soup = BeautifulSoup(page.content, "html.parser")
                    
                    # Find live match sections
                    match_containers = soup.find_all(class_="cb-mtch-lst cb-col cb-col-100 cb-tms-itm")
                    
                    if not match_containers:
                        raise Exception("No live matches found")
                        
                    # Get first live match
                    first_match = match_containers[0]
                    
                    # Extract team names
                    teams = first_match.find_all(class_="cb-ovr-flo cb-hmscg-tm-nm")
                    team1 = teams[0].get_text().strip() if len(teams) > 0 else "Team 1"
                    team2 = teams[1].get_text().strip() if len(teams) > 1 else "Team 2"
                    
                    # Extract scores
                    scores = first_match.find_all(class_="cb-ovr-flo")
                    team1_score = scores[0].get_text().strip() if len(scores) > 0 else "N/A"
                    team2_score = scores[1].get_text().strip() if len(scores) > 1 else "N/A"

                    notification.notify(
                        title="IPL SCORE",
                        message=f"{team1}: {team1_score}\n{team2}: {team2_score}",
                        timeout=15
                    )
                    speak(f"Current score is {team1} at {team1_score} and {team2} at {team2_score}")

                except Exception as e:
                    speak("Sorry, I couldn't fetch the live scores right now. Please check internet connection or try again later.")
                    print(f"Error: {str(e)}")

#Google Search
            elif 'search' in self.query:
                import wikipedia as googleScrap
                self.query = self.query.replace('search', '   ')
                self.query = self.query.replace('google search', '    ')
                self.query = self.query.replace('google','    ')
            
                speak('Here are some results...')

                try:
                    pywhatkit.search(self.query)
                    result = googleScrap.summary(self.query,3)
                    speak(result)

                except:
                    speak(' Data not cached..')
                    
#my location
            elif 'my location' in self.query:
                from Features import My_Location
                My_Location()  

#windows automation
            elif 'home screen' in self.query:
                from Features import WindowsAuto
                WindowsAuto(self.query)

            elif 'minimise' in self.query:
                from Features import WindowsAuto
                WindowsAuto(self.query)

            elif 'show start' in self.query:
                from Features import WindowsAuto
                WindowsAuto(self.query)

            elif 'open setting' in self.query:
                from Features import WindowsAuto
                WindowsAuto(self.query)

            elif 'restore windows' in self.query:
                from Features import WindowsAuto
                WindowsAuto(self.query)                  

#internet speed        
            elif "internet speed" in self.query:
                try:
                    import speedtest
                    speak("Checking internet speed... This may take a moment")
                    st = speedtest.Speedtest()
                    st.get_best_server()
                    download_speed = st.download() / 1_000_000  
                    upload_speed = st.upload() / 1_000_000      
                    download = f"{download_speed:.2f}"
                    upload = f"{upload_speed:.2f}"
                    
                    print(f"Download Speed: {download} Mbps")
                    print(f"Upload Speed: {upload} Mbps")
                    speak(f"Your current internet speed is {download} megabits per second download, and {upload} megabits per second upload")

                except Exception as e:
                    print(f"Speed test failed: {str(e)}")
                    speak("Sorry, I couldn't check the internet speed at this moment")

#screenshot              
            elif "screenshot" in self.query:
                try:
                    from datetime import datetime
                    
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    filename = f"screenshot_{timestamp}.jpg"
                    
                    im = pyautogui.screenshot()
                    im.save(filename)
                    
                    speak(f"Screenshot captured and saved as {filename}")
                    print(f"Screenshot saved successfully as {filename}")
                
                except Exception as e:
                    speak("Failed to capture screenshot")
                    print(f"Screenshot error: {str(e)}")

# Schedule Function
            elif "schedule my day" in self.query:
                    tasks = []
                    speak("Do you want to clear old tasks? Please say YES or NO.")
                    response = self.takeCommand().lower()
                    if "yes" in response:
                        with open("tasks.txt", "w") as file:
                            file.write("")
                        speak("Old tasks have been cleared.")
                    else:
                        speak("Old tasks will not be cleared.")

                    speak("How many tasks do you want to add?")
                    try:
                        no_tasks = int(self.takeCommand())  # Convert voice input to an integer
                    except ValueError:
                            speak("I couldn't understand the number of tasks. Please try again.")
                            no_tasks = 0  # Default to 0 if there's an error

                    if no_tasks > 0:
                        for i in range(no_tasks):
                            speak(f"Please tell me task number {i + 1}.")
                            task = self.takeCommand()  # Get task via voice input
                            if task:
                                tasks.append(task)
                                with open("tasks.txt", "a") as file:
                                    file.write(f"{i + 1}. {task}\n")
                                speak(f"Task {i + 1} added.")
                            else:
                                speak("I didn't hear the task clearly. Skipping this one.")

                    if tasks:
                        speak("Your tasks for today have been saved successfully.")
                    else:
                        speak("No tasks were added.")

#Schedule notification 
            elif "show my schedule" in self.query:
                file = open("tasks.txt","r")
                content = file.read()
                file.close()
                mixer.init()
                mixer.music.load("notification.mp3")
                mixer.music.play()
                notification.notify(
                    title = "My schedule :-",
                    message = content,
                    timeout = 15
                            )

#How to 
            elif 'how to' in self.query:
                speak('Searching for best results.....')
                op = self.query.replace("VirtuMate","   ")
                max_result = 1
                how_to_func = search_wikihow(op,max_result)
                assert len (how_to_func) == 1
                how_to_func[0].print()
                speak(how_to_func[0].summary)


#Open any app 
            elif "open" in self.query:
                import subprocess
                app_name = self.query.replace("open", "").strip()
                if app_name:
                    speak(f"Opening {app_name}")
                    try:
                        pyautogui.press("win")  
                        pyautogui.typewrite(app_name)  
                        pyautogui.sleep(1) 
                        pyautogui.press("enter")
                        speak(f"{app_name} is now open.")
                    except Exception as e:
                        speak(f"Sorry, I couldn't open {app_name}. Error: {str(e)}")
                else:
                    speak("Please specify the application to open.")

#close any app 
            elif "close" in self.query:
                  
                import psutil
                import os
                
                app_name = self.query.replace("close", "").strip()

                if app_name:
                    speak(f"Closing {app_name}")
                    found = False
                    for process in psutil.process_iter(['name']):
                        if app_name.lower() in process.info['name'].lower():
                            os.system(f"C:\\Windows\\System32\\taskkill.exe /F /IM {process.info['name']}")
                            speak(f"{app_name} has been closed.")
                            found = True
                            break
                    
                    if not found:
                        speak(f"Could not find {app_name} running.")
                else:
                    speak("Please specify the application to close.")


#Youtube automate
            elif "pause" in self.query:
                pyautogui.press("k")
                speak("video paused")
            elif "play" in self.query:
                pyautogui.press("k")
                speak("video played")
            elif "mute" in self.query:
                pyautogui.press("m")
                speak("video muted")
            elif "volume up" in self.query:
                from custom_keyboard import volumeup
                speak("Turning volume up")
                volumeup()
            elif "volume down" in self.query:
                from custom_keyboard import volumedown
                speak("Turning volume down")
                volumedown()    

#News function  
            elif "news" in self.query:
                from NewsRead import latestnews
                latestnews()

#NASA News
            elif 'space news' in self.query:
                speak('Say the date separated by And. For example 2021 and 12 and 09')

                Date = self.takeCommand()
                from Features import Dateconverter
                value = Dateconverter(Date)
                from Nasa import NasaNews
                NasaNews(value)

# System shutdown using voice command
            elif "shutdown the system" in self.query:
                speak("Are you sure you want to shutdown? Please say yes or no.")
                
                shutdown = self.takeCommand().lower() 
                
                if "yes" in shutdown: 
                    try: 
                        os.system("C:\\Windows\\System32\\shutdown.exe /s /t 1")
                        speak("Shutting down your system. Goodbye!")
                    except Exception as e:
                        print(f"Error: {e}")
                        speak("Failed to initiate shutdown. Please try manually.")
                
                elif "no" in shutdown:
                    speak("Shutdown cancelled.")
                
                else:
                    speak("I couldn't understand your response. Shutdown aborted.")

#Demonstration
            elif 'subscribe' in self.query:
                speak("Sure, I will show you how to subscribe to a channel on youtube.")
                speak("Firstly Go to youtube")
                webbrowser.open("https://www.youtube.com/")
                time.sleep(5)  # Wait for YouTube page to load
                speak("click on the search bar")
                pyautogui.moveTo(806, 125, 1)  # Move to search bar over 1 second
                pyautogui.click(x=806, y=125, clicks=1, interval=0, button='left')
                time.sleep(1)  # Small pause after clicking
                speak("Type the name of the channel that you want, for example i will type telusko")
                pyautogui.typewrite("telusko", 0.1)  # Type with 0.1s interval between keys
                time.sleep(2)  # Wait for typing to finish
                speak("press enter")
                pyautogui.press('enter')
                time.sleep(5)  # Wait for search results to load
                speak("Here you will see the list of channels")
                pyautogui.moveTo(971, 314, 1)  # Move to channel list area
                time.sleep(1)  # Pause to show the movement
                speak("click here to subscribe to the channel")
                pyautogui.moveTo(1830, 414, 1)  # Move to subscribe button
                pyautogui.click(x=1830, y=414, clicks=1, interval=0, button='left')
                time.sleep(1)  # Pause after subscribing
                speak("And also Don't forget to press the bell icon")
                pyautogui.moveTo(1750, 314, 1)  # Move to bell icon
                pyautogui.click(x=1750, y=314, clicks=1, interval=0, button='left')
                time.sleep(0.5)  # Wait for bell menu to appear
                speak("turn on all notifications")
                pyautogui.click(x=1750, y=320, clicks=1, interval=0, button='left')


#Execution UI        
startExecution = MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_jarvisUi()
        self.ui.setupUi(self)
        self.chatbot_active = False  # Flag to track chatbot state

        # Connect UI elements
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)
        self.ui.inputBox.returnPressed.connect(self.processUserInput)

        # Redirect standard output to UI terminal
        sys.stdout = self
        sys.stderr = self

    def processUserInput(self):
        """Capture user input from the text box and process it"""
        user_input = self.ui.inputBox.text().strip()
        if user_input:
            self.updateTerminal(f"User: {user_input}")
            if self.chatbot_active:
                if user_input.lower() in ["exit", "quit"]:
                    self.chatbot_active = False
                    startExecution.chatbot_active = False  # Sync with MainThread
                    response = "Chatbot deactivated."
                else:
                    # Run chatbot interaction in a separate thread
                    threading.Thread(target=self.chatbot_interaction, args=(user_input,), daemon=True).start()
            else:
                response = self.handleCommand(user_input)
                self.updateTerminal(f"Jarvis: {response}")
            self.ui.inputBox.clear()

    def handleCommand(self, command):
        """Process standard commands"""
        if command.lower() in ["let's chat", "can we talk"]:
            self.chatbot_active = True
            return "Chatbot activated. Please type your messages."
        elif command.lower() == "hello":
            return "Hello! How can I assist you?"
        elif command.lower() == "exit":
            self.close()
            return "Goodbye!"
        return "I didn't understand that command."

    def chatbot_interaction(self, user_input):
        """Handle chatbot interactions using text input in a separate thread"""
        from VirtuMateChatbot import chatbot_input
        response = chatbot_input(user_input)
        self.updateTerminal(f"Jarvis: {response}")

    def updateTerminal(self, message):
        """Append text to the output display (terminal)"""
        self.ui.outputDisplay.append(message)

    def write(self, message):
        """Redirect standard output to terminal display"""
        self.updateTerminal(message.strip())

    def flush(self):
        """Flush method to prevent buffering issues (needed for sys.stdout redirection)"""
        pass


    def startTask(self):
        self.chatbot_active = True
        self.ui.outputDisplay.append("Jarvis: Chatbot activated.")
        self.ui.movie = QtGui.QMovie("C:/Users/ADMIN/OneDrive/Desktop/ai model 1/Jarvis-AI-main/Material/new.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("C:/Users/ADMIN/OneDrive/Desktop/ai model 1/Jarvis-AI-main/Material/path.gif")
        self.ui.label_3.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("C:/Users/ADMIN/OneDrive/Desktop/ai model 1/Jarvis-AI-main/Material/logo.gif")
        self.ui.label_5.setMovie(self.ui.movie)
        self.ui.movie.start()
        startExecution.start()

    def chatbot_trigger(self):
        speak("Chatbot is now active. How can I assist you?")

app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(app.exec_())
