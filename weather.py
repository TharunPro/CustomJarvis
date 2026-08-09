import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_weather(city):
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(url, params=params, timeout=5)
        data = response.json()

        if response.status_code != 200:
            return f"I couldn't find weather for {city}."

        temp = round(data["main"]["temp"])
        description = data["weather"][0]["description"]
        return f"It's currently {temp} degrees in {city}, with {description}."

    except requests.exceptions.RequestException:
        return "I can't reach the weather service right now — check your internet connection."
