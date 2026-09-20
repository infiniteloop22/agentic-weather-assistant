import json
import ollama

class Model:
    def __init__(self, fetcher):
        self.fetcher = fetcher

    def query_model(self, user_input):
        weather_tool_definition = {
        'type': 'function',
        'function': {
            'name': 'fetch_live_weather',
            'description': 'Get the current real-time weather metrics for a specific city location.',
            'parameters': {
                'type': 'object',
                'properties': {
                    'city': {
                        'type': 'string',
                        'description': 'The name of the city, e.g., Austin, London, Paris',
                        },
                    },
                    'required': ['city'],
                },
            },
        }

        messages = [{'role': 'user', 'content': user_input}]

        response = ollama.chat(
            model='llama3.2:1b',
            messages=messages,
            tools=[weather_tool_definition]
        )

        if response.get('message', {}).get('tool_calls'):
            for tool in response['message']['tool_calls']:
                if tool['function']['name'] == 'fetch_live_weather':
                    extracted_city = tool['function']['arguments']['city']
                    print(f"Triggered model tool 'fetch_live_weather' for city: '{extracted_city}'")
                    
                    weather_results = self.fetcher.get_weather_data(extracted_city)
                    
                    messages.append(response['message'])
                    messages.append({
                        'role': 'tool',
                        'content': json.dumps(weather_results),
                        'name': 'fetch_live_weather'
                    })
                    
            final_response = ollama.chat(model='llama3.2:1b', messages=messages)
            return final_response['message']['content']
            
        else:
            return final_response['message']['content']