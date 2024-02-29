# Programmer: Brysom LaMew
# Date: 2.29.24
# Program: AI Playground
"""
pip install requests

def get_weather(api_key, city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()
    if data['cod'] == 200:
        weather_info = {
            'city': data['name'],
            'description': data['weather'][0]['description'],
            'temperature': data['main']['temp'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed']
        }
        return weather_info
    else:
        return None

def main():
    api_key = 'd3012a6aae9325513f1c02b62cfdb603'  # Replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key
    city = input("Enter city name")
    weather = get_weather(api_key, city)
    if weather:
        print(f"Weather in {weather['city']}:")
        print(f"Description: {weather['description']}")
        print(f"Temperature: {weather['temperature']}°C")
        print(f"Humidity: {weather['humidity']}%")
        print(f"Wind Speed: {weather['wind_speed']} m/s")
    else:
        print("Failed to fetch weather information.")

if __name__ == "__main__":
    main()
```

To use this program:

1. You'll need to sign up for an account and get an API key from OpenWeatherMap (https://openweathermap.org/api).
2. Replace `'YOUR_API_KEY'` with your actual API key.
3. Run the script, and it will prompt you to enter the city name.
4. It will then fetch and display the current weather information for that city.

Make sure you have the `requests` library installed. You can install it via pip if you don't have it already:

```
pip install requests
```
print("This will be a place for me to play with programming using AI Technology\n")

import requests

def get_weather(api_key, city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()
    if data['cod'] == 200:
        weather_info = {
            'city': data['name'],
            'description': data['weather'][0]['description'],
            'temperature': data['main']['temp'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed']
        }
        return weather_info
    else:
        return None

def main():
    api_key = 'd3012a6aae9325513f1c02b62cfdb603'  # Replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key
    city = input("Enter city name: ")
    weather = get_weather(api_key, city)
    if weather:
        print(f"Weather in {weather['city']}:")
        print(f"Description: {weather['description']}")
        print(f"Temperature: {weather['temperature']}°C")
        print(f"Humidity: {weather['humidity']}%")
        print(f"Wind Speed: {weather['wind_speed']} m/s")
    else:
        print("Failed to fetch weather information.")

if __name__ == "__main__":
    main()
"""

import urllib.parse
import urllib.request
import json

def get_weather(api_key, city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    try:
        with urllib.request.urlopen(url) as response:
            data = response.read().decode('utf-8')
            weather_info = json.loads(data)
            if weather_info['cod'] == 200:
                return {
                    'city': weather_info['name'],
                    'description': weather_info['weather'][0]['description'],
                    'temperature': weather_info['main']['temp'],
                    'humidity': weather_info['main']['humidity'],
                    'wind_speed': weather_info['wind']['speed']
                }
            else:
                return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def main():
    api_key = 'd3012a6aae9325513f1c02b62cfdb603'  # Replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key
    city = input("Enter city name: ")
    weather = get_weather(api_key, city)
    if weather:
        print(f"Weather in {weather['city']}:")
        print(f"Description: {weather['description']}")
        print(f"Temperature: {weather['temperature']}°C")
        print(f"Humidity: {weather['humidity']}%")
        print(f"Wind Speed: {weather['wind_speed']} m/s")
    else:
        print("Failed to fetch weather information.")

if __name__ == "__main__":
    main()