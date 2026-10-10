import json
import ollama
from pydantic import BaseModel, Field

class WeatherQuery(BaseModel):
    city: str = Field(description="The name of the city (Berlin, Paris, London).")

class Model:
    def __init__(self, fetcher):
        self.fetcher = fetcher

    def query_model(self, user_input):
        messages = [{'role': 'user', 'content': user_input}]

        response = ollama.chat(
            model='llama3.2:1b',
            messages=messages,
            format=WeatherQuery.model_json_schema()
        )

        structured_data = WeatherQuery.model_validate_json(response['message']['content'])
        extracted_city = structured_data.city

        print(f"\nQuerying for {extracted_city}...")

        weather_results = self.fetcher.get_weather_data(extracted_city)

        final_prompt = (
                f"User Question: {user_input}\n\n"
                f"Live Weather Data to use for your answer:\n"
                f"{json.dumps(weather_results, indent=2)}\n\n"
                f"Answer the user's question naturally using the data provided. "
                f"Do not output JSON or dictionaries. Just reply with conversational text."
            )

        final_messages = [{'role': 'user', 'content': final_prompt}]
            
        final_response = ollama.chat(
            model='llama3.2:1b',
            messages=final_messages
        )

        print()
            
        return final_response['message']['content']
