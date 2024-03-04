
import requests

def fetch_weather_data(city):
    # Replace 'YOUR_API_KEY' with your actual API key
    api_key = 'YOUR_API_KEY'
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }
    response = requests.get(base_url, params=params)
    if response.status_code ==  200:
        return response.json()
    else:
        return None


def display_weather_data(weather_data):
    if weather_data:
        main_weather = weather_data['weather'][0]['main']
        description = weather_data['weather'][0]['description']
        temperature = weather_data['main']['temp']
        print(f"Weather in {weather_data['name']}: {main_weather} - {description}")
        print(f"Temperature: {temperature}°C")
    else:
        print("Could not fetch weather data.")
        

def main():
    city = input("Enter the city name: ")
    weather_data = fetch_weather_data(city)
    display_weather_data(weather_data)

if __name__ == "__main__":
    main()