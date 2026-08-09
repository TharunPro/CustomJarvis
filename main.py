import pyfiglet
from voice import speak, listen, console  # Voice System
from skills import (
    greet, show_help, tell_time, tell_date,
    open_site, open_app,
    TIME_TRIGGERS, DATE_TRIGGERS, SITE_TRIGGERS, APP_TRIGGERS, HELP_TRIGGERS, EXIT_TRIGGERS
) # Skills for J.A.R.V.I.S
from sites import SITES # Websites
from apps import APPS # Applications
from rich.panel import Panel # Rich Panel for UI


console.print(
    pyfiglet.figlet_format("JARVIS", font="ansi_shadow", justify="center"),
    style="cyan"
)

def handle_command(prompt):
    if prompt.startswith("open "):
        target = prompt[5:].strip()
        if target in SITES:
            open_site(target)
        elif target in APPS:
            open_app(target)
        else:
            speak("I don't know that site or app yet.")
    elif any(word in prompt for word in HELP_TRIGGERS):
        show_help()
    elif any(word in prompt for word in TIME_TRIGGERS):
        tell_time()
    elif any(word in prompt for word in DATE_TRIGGERS):
        tell_date()
    elif any(word in prompt for word in SITE_TRIGGERS):
        open_site()
    elif any(word in prompt for word in APP_TRIGGERS):
        open_app()
    else:
        speak("I didn't catch that. Say help to see what I can do.")

def main():
    greet()

    while True:
        prompt = listen()
        if not prompt:
            continue
        if any(word in prompt for word in EXIT_TRIGGERS):
            speak("See you later!")
            break
        handle_command(prompt)

if __name__ == "__main__":
    main()