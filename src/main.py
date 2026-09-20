import json
from weather import WeatherFetcher
from model import Model

def load_api_key() -> str:
    with open('src/config.json', 'r') as file:
        config = json.load(file)

    return config["API_WEATHER_KEY"]

def main():
    api_key = load_api_key()
    fetcher = WeatherFetcher(api_key)
    query = Model(fetcher)

    while True:
        user_input = input("Query the LLM (Should I wear a coat outside in Oslo?): ")
        if user_input == "exit":
            break

        print(query.query_model(user_input))

if __name__ == "__main__":
    main()