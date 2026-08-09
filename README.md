# CustomJarvis

A personal voice assistant built in Python — inspired by JARVIS, built from scratch as a learning project. Speaks back with text-to-speech, listens via your microphone, and runs custom "skills" for everyday tasks.

## Features

* 🎙️ Voice input via microphone (Google Speech Recognition)
* 🔊 Spoken responses via text-to-speech (`pyttsx3`)
* 🕒 Tells the current time and date
* 🌡️ Tells the temperature of any city
* 🌐 Opens websites by voice ("open youtube")
* 🖥️ Opens desktop apps by voice ("open notepad", "launch calculator")
* 🎨 Styled terminal output via `rich`
* 🧩 Clean, modular file structure — easy to add new skills

## Project structure

```
CustomJarvis/
├── main.py       # entry point, command routing loop
├── skills.py     # all skill functions + trigger words
├── voice.py      # speak() / listen() — speech recognition \& TTS
├── sites.py      # dictionary of website shortcuts
├── apps.py       # dictionary of desktop app shortcuts
└── .gitignore
```

## Setup

1. Clone the repo:

```bash
   git clone https://github.com/yourusername/CustomJarvis.git
   cd CustomJarvis
   ```

2. Install dependencies:

```bash
   pip install SpeechRecognition pyttsx3 pyaudio rich
   ```

3. Run it:

```bash
   python main.py
   ```

## Usage

Once running, just talk to it. Try:

* "what can you do?"
* "what time is it?"
* "today's date"
* "open youtube"
* "open notepad"
* "help"
* "exit" / "quit" to stop

## Notes

Built as a personal learning project, starting simple and adding one skill at a time.

