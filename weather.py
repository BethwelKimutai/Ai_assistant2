import geocoder
import requests

from speak import Say


def get_location():
    g = geocoder.ip('me')
    return g.city


def get_weather(api_key, city):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        main_weather = data['weather'][0]['main']
        description = data['weather'][0]['description']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        return {
            "main": main_weather,
            "description": description,
            "temperature": temperature,
            "humidity": humidity
        }
    else:
        return None


if __name__ == "__main__":
    api_key = "36aaa00e51fa8a07bf5e7c29524ad68e"

    # Automatically get your location based on IP
    city = get_location()

    if city:
        Say("Your Current Location:", city)

        weather_data = get_weather(api_key, city)

        if weather_data:
            Say("Weather Update for", city)
            Say("Main Weather:", weather_data["main"])
            Say("Description:", weather_data["description"])
            Say("Temperature:", f"{weather_data['temperature']} degrees Celsius")
            Say("Humidity:", f"{weather_data['humidity']} percent")
        else:
            Say("Failed to retrieve weather data for your location.")
    else:
        Say("Failed to determine your location.")
