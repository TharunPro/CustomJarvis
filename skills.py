import datetime
import pyautogui
import ctypes
import sys
import os
import webbrowser
import urllib.parse
import winshell
import pyjokes
import psutil
from rich.console import Console
from apps import APPS
from sites import SITES
from weather import get_weather
from voice import speak, listen

console = Console()

def convertTime(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return "%d:%02d:%02d" % (hours, minutes, seconds)

# Basic Skills

def greet():
    hour = datetime.datetime.now().hour
    #speak("What is your name?")
    #name = listen()
    if 5 <= hour < 12:
        greeting = "Good morning"
    elif 12 <= hour < 18:
        greeting = "Good afternoon"
    else:
        greeting = "Good evening"
    speak(f"{greeting} Sir, what should we do today?")

def show_help():
    console.print("[bold cyan]Custom Jarvis Features[/bold cyan]")
    console.print("[green]•[/green] Time and date")
    console.print("[green]•[/green] Weather by city")
    console.print("[green]•[/green] Web search")
    console.print("[green]•[/green] Open websites")
    console.print("[green]•[/green] Open apps")
    console.print("[green]•[/green] Lock PC")
    console.print("[green]•[/green] Empty recycle bin")
   
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

def tell_joke():
    joke = pyjokes.get_joke()
    speak(joke)

# Web & App Skills

def search_web(prompt=None):
    query = None
    if prompt:
        for trigger in ("search for", "google", "search"):
            if trigger in prompt:
                query = prompt.split(trigger, 1)[-1].strip()
                break

    if not query:
        query = listen_for("What should I search for?")

    if not query:
        return

    url = f"https://www.google.com/search?q={urllib.parse.quote_plus(query)}"
    webbrowser.open(url)
    speak(f"Searching for {query} on Google.")
    
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
# System Skills

def screenshot():
    speak("Taking a screenshot now.")
    target = os.path.expanduser("~/Pictures/Screenshots")
    os.makedirs(target, exist_ok=True)

    now = datetime.datetime.now()
    timestamp = now.strftime('%B_%d_%Y_%H-%M-%S')
    filename = f"screenshot_{timestamp}.png"
    full_path = os.path.join(target, filename)
    pyautogui.screenshot(full_path)
    speak(f"Screenshot saved as {full_path}")

def empty_recycle_bin():
    speak("Are you sure you want to empty the recycle bin?")
    confirmation = listen()
    if confirmation and "yes" in confirmation:
        try:
            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
            speak("I successfully emptied the recycle bin.")
        except Exception:
            speak("I couldn't empty the recycle bin.")

    else:
        speak("Okay I won't empty the recycle bin.")

def lock_pc():
    speak("Locking your PC now. Goodbye Sir.")
    ctypes.windll.user32.LockWorkStation()
    sys.exit()

def show_battery_status():
    battery = psutil.sensors_battery()
    if battery:
        percent = battery.percent
        plugged = battery.power_plugged
        status = "charging" if plugged else "not charging"
        speak(f"The battery is at {percent}%, is currently {status} and still has {convertTime(battery.secsleft)}s left.")
    else:
        speak("I couldn't retrieve the battery status.")


def listen_for(question):
    speak(question)
    answer = listen().rstrip(".,!?")
    return answer.strip().lower() if answer else ""

EXIT_TRIGGERS = ["exit", "quit", "stop", "goodbye", "bye"]

COMMAND_MAP = {
    # Basic Features

    "time": (tell_time, False),
    "date": (tell_date, False),
    "weather": (tell_weather, True),
    "forecast": (tell_weather, True),
    "temperature": (tell_weather, True),
    "help": (show_help, False),
    "what can you do": (show_help, False),
    "features": (show_help, False),
    "joke": (tell_joke, False),
    # Web & App Skills

    "app": (open_app, False),
    "application": (open_app, False),
    "program": (open_app, False),
    "launch": (open_app, False),
    "site": (open_site, False),
    "website": (open_site, False),
    "webpage": (open_site, False),
    "search": (search_web, True),
    "google": (search_web, True),
    # System Skills

    "lock": (lock_pc, False),
    "screenshot": (screenshot, False),
    "screen shot": (screenshot, False),
    "recycle bin": (empty_recycle_bin, False),
    "recycle": (empty_recycle_bin, False),
    "battery": (show_battery_status, False),
    "percentage": (show_battery_status, False),
}