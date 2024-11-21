import datetime
import webbrowser
from platform import platform

import speech_recognition as sr
import win32com.client
#from playsound import playsound
import subprocess
import argparse
from openai import OpenAI
import os
import sys
import pyautogui
import pywhatkit
from openai import OpenAI
from playsound import playsound
from PyQt5 import QtCore, QtGui, QtWidgets
import platform
from PyQt5.QtCore import QTime,QTimer ,QDate,Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from JARVIS_GUI import Ui_Dialog
from pygame.examples.vgrade import timer

client = OpenAI(
    api_key = "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",
)

speaker = win32com.client.Dispatch('SAPI.SpVoice')

def ai(prompt):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    client = OpenAI()

    completion = client.chat.completions.create(
        model="gpt-4o",

        messages=[{"role": "system",
                   "content": "Please act as an AI assistant named Jarvis created by 'KAPIL DAS'. Listen and respond to user commands and inquiries in a helpful and efficient manner. Perform tasks such as setting reminders, answering questions, providing information, and executing basic tasks. Use a friendly and professional tone throughout."},
                  {"role": "user", "content": prompt}],

    )

    print(completion.choices[0].message)
    print(text1)
    speaker.speak(text1)
    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    with open(f"Openai/{prompt}  .txt", "w") as f:
        f.write(text1)


def speak():
    while 1:
        print("WRITE!!!")
        S = input()
        speaker.Speak(S)




def wishMe():
        hour = int(datetime.datetime.now().hour)
        if hour >= 0 and hour < 12:
            speaker.speak("Good Morning sir")

        elif hour >= 12 and hour < 18:
            speaker.speak("Good Afternoon sir")

        else:
            speaker.speak("Good Evening sir")


def takeCommand():
        # It takes microphone input from the user and returns string output

        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")

        except Exception as e:
            # print(e)
            print("Say that again please...")
            return "None"
        return query
def openapps():
       if "open files explorer".lower() in w.lower() or "open files" in w:
            print("Try to open File Explorer")

            os.system("start explorer")
            print("File Explorer opened")
            speaker.speak("File Explorer opened")

       elif "open calculator".lower() in w.lower():
        print("Try to open Calculator")

        os.system("start calc")
        print("Calculator opened")
        speaker.speak("Calculator opened")

       elif "open command prompt".lower() in w.lower():
        print("Try to open Command Prompt")

        os.system("start cmd")
        print("Command Prompt opened")
        speaker.speak("Command Prompt opened")







speaker.speak("Hello,Kapil Sir I am your A I Jarvis")
wishMe()

w = takeCommand()


def openwebs():
    sites = [["facebook", "https://www.facebook.com"],
        ["whatsapp", "https://www.whatsapp.com"],
        ["instagram", "https://www.instagram.com"],
        ["cricbuzz", "https://www.cricbuzz.com"],
        ["gaana", "https://gaana.com"],
        ["hotstar", "https://www.hotstar.com"],
        ["bookmyshow", "https://www.bookmyshow.com"],
        ["makemytrip", "https://www.makemytrip.com"],
        ["zomato", "https://www.zomato.com"],
        ["swiggy", "https://www.swiggy.com"],
        ["phonepe", "https://www.phonepe.com"],
        ["paytm", "https://paytm.com"],
        ["chatgpt", "https://www.chatbot.com"],
        ["stackoverflow", "https://stackoverflow.com"],
        ["spotify", "https://www.spotify.com"],
        ["github", "https://www.github.com"],
        ["google maps", "https://www.google.com/maps"],
        ["duckduckgo", "https://duckduckgo.com"],
        ["linkedin", "https://www.linkedin.com"],
        ["reddit", "https://www.reddit.com"],
        ["netflix", "https://www.netflix.com"],
        ["ebay", "https://www.ebay.com"],
        ["microsoft", "https://www.microsoft.com"],
        ["apple", "https://www.apple.com"],
        ["pinterest", "https://www.pinterest.com"],
        ["yandex", "https://www.yandex.ru"],
        ["bing", "https://www.bing.com"],
        ["aliexpress", "https://www.aliexpress.com"],
        ["zoom", "https://www.zoom.ind"],
        ["wordpress", "https://www.wordpress.com"],
        ["snapchat", "https://www.snapchat.com"],
        ["weather", "https://www.weather.com"]]

    for site in sites:
        if f"Open {site[0]}".lower() in w.lower():
            speaker.speak(f"opening {site[0]}  sir")
            webbrowser.open(site[1])



def playsongs():
 if "play" in w.lower():
    song = w.replace("play", "")
    song = w.replace("jarvis" ,"")
    speaker.speak("playing " + song)
    pywhatkit.playonyt(song)
    while True:

        query = takeCommand().lower()
        if "pause" in query or "stop" in query:
            pyautogui.press("k")
            speaker.speak("video paused")
        elif any(keyword in query for keyword in ["on", "start", "play"]):
            pyautogui.press("k")
            speaker.speak("video played")
        elif "mute" in query:
            pyautogui.press("m")
            speaker.speak("video muted")
        elif "unmute" in query:
            pyautogui.press("m")
            speaker.speak("video unmuted")
        elif "volume up" in query:
            speaker.speak("Turning volume up, sir")
            volumeup()
        elif "volume down" in query:
            speaker.speak("Turning volume down, sir")
            volumedown()

def time():
    if "Time".lower() in w.lower():
        StrfTime = datetime.datetime.now().strftime("%H:%M:%S")
        speaker.speak(f"{StrfTime}")










def openai():
    if "use your intelligence".lower() in w.lower():
        ai(prompt=w)

def stop():
    if "quit" in w.lower():
        exit()


if __name__ == '__main__':
    stop()
    while True:
        w = takeCommand()
        openapps()
        openai()
        openwebs()
        time()
        playsongs()


