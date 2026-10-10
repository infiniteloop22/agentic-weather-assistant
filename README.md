# Conversational OpenWeather AI Pipeline

A Python application using local LLMs via **Ollama** and **Pydantic** for structured outputs to parse conversational queries and fetch OpenWeather data.

## Features
- **Processing:** Uses `llama3.2:1b` with Pydantic for parameter validation.
- **AI Pipeline:** Extracts locations, queries data, and returns conversational responses.
- **Data Logging:** Logs data into a local text file 'weather_data.txt'.

## Technologies Used
- Python 3.8+, `ollama` (`llama3.2:1b`), `pydantic`, `requests`, and OpenWeather API.

## Prerequisites & Installation
1. Ensure Python 3.8+, an OpenWeather API key, and [Ollama](https://ollama.com) are installed, then pull the model:
   ```bash
   ollama pull llama3.2:1b
   ```
2. Clone the repository and activate your virtual environment:
   ```bash
   git clone https://github.com/infiniteloop22/agentic-weather-assistant
   cd agentic-weather-assistant
   # Activate venv: source .venv/bin/activate (Mac/Linux) or .\.venv\Scripts\Activate.ps1 (Windows)
   ```
3. Install dependencies and set your API key:
   ```bash
   pip install -r requirements.txt
   # Create a config.json file and set your API key in the file like this:
   # { 
   #    "API_WEATHER_KEY": "insert key here"
   # }
   ```

## Usage
Run `python main.py` and ask a conversational question when prompted.