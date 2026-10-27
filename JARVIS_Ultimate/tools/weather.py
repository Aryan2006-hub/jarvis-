import requests
from config import OPENWEATHER_API_KEY

def get_weather(city):
    if not OPENWEATHER_API_KEY:
        return None, "Weather API key is not configured."
    try:
        url = "https://api.openweathermap.org/data/2.5/weather"
        data = requests.get(url, params={
            "q": city, "appid": OPENWEATHER_API_KEY, "units": "metric"
        }, timeout=8).json()
        if data.get("cod") != 200:
            return None, data.get("message", "Weather lookup failed.")
        desc = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        feels = data["main"]["feels_like"]
        return {"city": city, "temp": temp, "feels": feels, "description": desc}, None
    except Exception as exc:
        return None, str(exc)
