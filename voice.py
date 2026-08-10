import speech_recognition as sr
import pyttsx3
import whisper
import numpy as np
from rich.console import Console

console = Console()
recognizer = sr.Recognizer()

JARVIS_VOICE_ID = r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"

console.print("[dim]Loading speech model...[/dim]")
whisper_model = whisper.load_model("base")
console.print("[dim]Model loaded.[/dim]")


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
        wav_data = audio.get_wav_data(convert_rate=16000, convert_width=2)
        audio_array = np.frombuffer(wav_data, np.int16).astype(np.float32) / 32768.0
        result = whisper_model.transcribe(audio_array, language="en", fp16=True)
        text = result["text"].strip()
        console.print(f"[green]You said:[/green] {text}")
        return text.lower()
    except Exception:
        speak("Sorry, I didn't catch that.")
        return ""