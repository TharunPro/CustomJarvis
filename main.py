import pyfiglet
from voice import speak, listen, console, tiny_model
from skills import (greet, open_site, open_app, EXIT_TRIGGERS, COMMAND_MAP) 
from sites import SITES # Websites
from apps import APPS # Applications
from rich.panel import Panel # Rich Panel for UI

console.print(
    pyfiglet.figlet_format("JARVIS", font="ansi_shadow", justify="center"),
    style="cyan"
)

def handle_command(prompt):
    prompt = prompt.strip().lower().replace("jarvis", "", 1).strip()
    prompt = prompt.strip(" ,.!?\"")

    if prompt.startswith("open "):
        target = prompt[5:].strip()
        if target in SITES:
            open_site(target)
        elif target in APPS:
            open_app(target)
        else:
            speak("I don't know that site or app yet.")
        return

    for keyword, (func, needs_prompt) in COMMAND_MAP.items():
        if keyword in prompt:
            func(prompt) if needs_prompt else func()
            return

    speak("I didn't catch that. Say help to see what I can do.")

def main():
    greet()
    while True:
        prompt = listen(tiny_model)
        if not prompt:
            continue
        if "jarvis" not in prompt:
            continue

        command = prompt.replace("jarvis", "", 1).strip().rstrip(".,!?")
        if not command:
            continue
        handle_command(command)

if __name__ == "__main__":
    main()