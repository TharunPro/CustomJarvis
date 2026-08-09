import datetime
import ctypes
import sys
import os
import webbrowser
from apps import APPS
from sites import SITES
from weather import get_weather
from voice import speak, listen

def greet():
    hour = datetime.datetime.now().hour
    if 5 <= hour < 12:
        greeting = "Good morning"
    elif 12 <= hour < 18:
        greeting = "Good afternoon"
    else:
        greeting = "Good evening"
    speak(f"{greeting} Sir, what should we do today?")

def show_help():
    speak("I can tell the time, tell you today's date, open websites, and open apps for you.")

def tell_time():
    now = datetime.datetime.now()
    speak(f"The current time is {now.strftime('%H:%M')}")

def tell_date():
    today = datetime.date.today()
    speak(f"Today's date is {today.strftime('%B %d, %Y')}")

def tell_weather(prompt=None):
    if prompt and " in " in prompt:
        city = prompt.split(" in ")[-1].strip()
    else:
        city = listen_for("Which city's weather should I fetch?")    

    if not city:
        return
    result = get_weather(city)                 
    speak(result)
    
def open_site(name=None):
    name = name or listen_for("Which website should I open?")
    if not name:
        return
    if name in SITES:
        webbrowser.open(SITES[name])
        speak(f"Opening {name}")
    else:
        speak("I don't know that one yet.")

def open_app(name=None):
    name = name or listen_for("Which app should I open?")
    if not name:
        return
    if name in APPS:
        try:
            os.startfile(APPS[name])
            speak(f"Opening {name}")
        except FileNotFoundError:
            speak(f"I couldn't find {name} on this system.")
    else:
        speak("I don't have that app yet.")

def lock_pc():
    speak("Locking your PC now. Goodbye Sir.")
    ctypes.windll.user32.LockWorkStation()
    sys.exit()


def listen_for(question):
    speak(question)
    answer = listen()
    return answer.strip().lower() if answer else ""

TIME_TRIGGERS = ["time"]
DATE_TRIGGERS = ["date"]
SITE_TRIGGERS = ["website", "site", "webpage"]
APP_TRIGGERS = ["app", "application", "program", "launch"]
HELP_TRIGGERS = ["help", "features"]
EXIT_TRIGGERS = ["exit", "quit", "stop", "goodbye", "bye"]
WEATHER_TRIGGERS = ["weather", "forecast", "temperature"]
LOCK_TRIGGERS = ["lock"]