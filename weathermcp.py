import os

import requests
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("weather")
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

@mcp.tool()
def get_current_weather(city: str) -> str:
    """Get current weather for a city.

    Args:
        city: Name of the city
            (e.g. 'Singapore', 'Tokyo')
    """

    base = (
        "https://api.openweathermap.org"
        "/data/2.5/weather"
    )
    url = (
        f"{base}?q={city}"
        f"&appid={WEATHER_API_KEY}"
        f"&units=imperial"
    )
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather = (
            data["weather"][0]["description"]
        )
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        return (
            f"The weather in {city} "
            f"is {weather} "
            f"with a temperature of "
            f"{temperature}°F, "
            f"humidity of {humidity}%, "
            f"and wind speed of "
            f"{wind_speed} mph"
        )
    else:
        return (
            f"Error {response.status_code}: "
            f"{response.json()}"
        )

if __name__ == "__main__":
    mcp.run()

