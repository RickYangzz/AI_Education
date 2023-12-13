# https://pypi.org/
# The Python Package Index (PyPI) is a repository
# of software for the Python programming language.

# https://home.openweathermap.org/
# OpenWeather is a team of IT experts and data scientists that has been 
# practising deep weather data science. For each point on the globe, 
# OpenWeather provides historical, current and forecasted weather data 
# via light-speed APIs. Headquarters in London, UK.

import requests
from dotenv import load_dotenv
import os
from pprint import pprint

load_dotenv()

def get_current_weather():
    print("\n*** Get Current Weather Conditions ***\n")
    city = input("\nPlease enter a city name: \n")

    request_url=f"https://api.openweathermap.org/data/2.5/weather?appid={os.getenv('API_KEY')}&q={city}&units=metric"

    try:
        weather_data = requests.get(request_url).json() 
    except:
        print("Current connection is not good, please try again.")
        return
    
    # pprint(weather_data)

    print(f"\nCurrent weather for {weather_data['name']}")
    print(f"The temp is {weather_data['main']['temp']}")
    print(f"Feels like {weather_data['main']['feels_like']} and {weather_data['weather'][0]['description']}")

    print("\n*** Thanks For Your Request ***\n")


if __name__ == "__main__":
    get_current_weather()