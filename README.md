# CustomJarvis

CustomJarvis is a Windows voice assistant inspired by J.A.R.V.I.S. It listens through your microphone, speaks back through text-to-speech, and runs a growing set of local and web-based skills.

This project is designed to be easy to understand and easy to extend. Each skill lives in a small, separate function so you can add new commands without rewriting the whole app.

## What it can do

- Greet you based on the time of day
- Tell the current time and date
- Fetch the weather for a city
- Search the web with Google
- Open websites like YouTube, GitHub, Gmail, and more
- Open desktop apps like Notepad, Calculator, Paint, Chrome, Discord, and Steam
- Take a screenshot
- Lock your PC
- Empty the Recycle Bin
- Show a quick help summary of available skills

## How it works

- `main.py` starts the assistant and keeps the command loop running
- `voice.py` handles microphone input and text-to-speech output
- `skills.py` contains the command logic and skill routing
- `sites.py` stores website shortcuts
- `apps.py` stores application shortcuts
- `weather.py` fetches weather data from OpenWeather

## Requirements

- Windows 10 or Windows 11
- Python 3.10 or newer recommended
- A working microphone
- Internet access for speech recognition, weather, and web search
- An OpenWeather API key for weather lookups

## Beginner-friendly setup

### 1. Download or clone the project

If you have Git installed, clone the repository:

```bash
git clone https://github.com/yourusername/CustomJarvis.git
cd CustomJarvis
```

If you already have the folder open, you can skip this step.

### 2. Create a virtual environment

This keeps the project dependencies separate from the rest of your system.

```bash
python -m venv .venv
.venv\Scripts\activate
```

If activation works, you should see `(.venv)` in your terminal.

### 3. Install the Python packages

Install the libraries used by the assistant:

```bash
pip install openai-whisper SpeechRecognition pyttsx3 pyautogui rich pyfiglet requests python-dotenv numpy winshell pyaudio
```

If `pyaudio` gives you trouble on Windows, install it with a prebuilt wheel that matches your Python version, or use a Windows-specific package manager such as `pipwin`.

### 4. Install FFmpeg

Whisper needs FFmpeg to process audio.

- Install FFmpeg on Windows
- Make sure `ffmpeg` is available in your PATH

If Whisper cannot start, FFmpeg is one of the first things to check.

### 5. Add your OpenWeather API key

Create a `.env` file in the project root if it is not already set up, then add:

```env
OPENWEATHER_API_KEY=your_api_key_here
```

You can get a key from OpenWeather.

### 6. Run the assistant

```bash
python main.py
```

When it starts, Jarvis will greet you and begin listening for commands.

## Example commands

Try saying things like:

- `what can you do`
- `what time is it`
- `what's the date`
- `weather in London`
- `search for python voice assistant`
- `open youtube`
- `open notepad`
- `open calculator`
- `take a screenshot`
- `lock the pc`
- `empty recycle bin`
- `exit`

## Available website shortcuts

The assistant knows shortcuts for many sites already, including Google, YouTube, Wikipedia, Maps, Reddit, X, Instagram, Facebook, LinkedIn, Discord, WhatsApp, Netflix, Spotify, Twitch, Gmail, Outlook, Google Drive, Notion, GitHub, Stack Overflow, ChatGPT, Claude, Amazon, Chess.com, Lichess, and Google News.

You can extend the list in [sites.py](sites.py).

## Available app shortcuts

The assistant can open several local apps already, including Notepad, Paint, Calculator, File Explorer, Chrome, Discord, Steam, and CapCut.

You can extend the list in [apps.py](apps.py).

## Project structure

```text
CustomJarvis/
├── main.py       # entry point and command loop
├── skills.py     # skill functions and command map
├── voice.py      # microphone input and text-to-speech
├── sites.py      # website shortcuts
├── apps.py       # desktop app shortcuts
├── weather.py    # weather API integration
├── skills.txt    # human-readable skill list
├── README.md     # project overview and setup guide
└── .gitignore
```

## Troubleshooting

- If Jarvis cannot hear you, check your microphone permissions and make sure the correct input device is selected.
- If startup fails around Whisper, verify that FFmpeg is installed and available in PATH.
- If weather commands do not work, confirm that `OPENWEATHER_API_KEY` is set in `.env`.
- If an app does not open, update its path in [apps.py](apps.py).
- If a website does not open, add or correct it in [sites.py](sites.py).

## Extending CustomJarvis

To add a new skill, create a function in [skills.py](skills.py) and add a trigger word or phrase to `COMMAND_MAP`.

To add a new app or website shortcut, add a new entry to [apps.py](apps.py) or [sites.py](sites.py).

## Notes

This is a personal learning project, but it is structured to stay readable as it grows. The current setup is intentionally simple so beginners can run it, inspect it, and modify it step by step.
