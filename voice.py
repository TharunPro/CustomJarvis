import speech_recognition as sr
import pyttsx3
from rich.console import Console

console = Console()
recognizer = sr.Recognizer()

JARVIS_VOICE_ID = r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"

def speak(text):
    console.print(f"[bold cyan]Jarvis:[/bold cyan] {text}")
    engine = pyttsx3.init()
    engine.setProperty('voice', JARVIS_VOICE_ID)
    engine.setProperty('rate', 170)
    engine.say(text)
    engine.runAndWait()
    engine.stop()

def listen():
    with sr.Microphone() as source:
        console.print("[dim]Listening...[/dim]")
        recognizer.adjust_for_ambient_noise(source, duration=1.2)
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        console.print(f"[green]You said:[/green] {text}")
        return text.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError:
        speak("Speech service is unavailable right now.")
        return ""