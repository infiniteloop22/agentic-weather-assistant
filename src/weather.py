import requests

class WeatherFetcher:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_weather_data(self, city):
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}&units=metric"

        response = requests.get(url)
        data = response.json()

        data_str = str(data)
        with open('src/weather_data.txt', 'w') as file:
            file.write(data_str)

        fahrenheit = (data["main"]["temp"] * (9/5)) +  32
        return {"city" : data["name"],
            "country" : data["sys"]["country"],
            "temperature_f" : round(fahrenheit, 1),
            "humidity" : data["main"]["humidity"],
            "wind_speed" : data["wind"]["speed"], 
            "weather conditions" : data["weather"][0]["description"],
            "timezone" : data["timezone"]
        }
