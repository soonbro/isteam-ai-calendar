import os.path
from dotenv import load_dotenv
from langchain_community.document_loaders import WeatherDataLoader

# .env 파일 환경변수 로드
load_dotenv()

"""
%pip install --upgrade --quiet  pyowm
"""

OPENWEATHERMAP_API_KEY=os.environ.get("OPENWEATHERMAP_API_KEY")

def get_weather_doc():
    """
    WeatherDataLoader [API Reference](https://api.python.langchain.com/en/latest/document_loaders/langchain_community.document_loaders.weather.WeatherDataLoader.html)
    """
    loader = WeatherDataLoader.from_params(
        ["seoul"], openweathermap_api_key=OPENWEATHERMAP_API_KEY
        )
    weather_documents = loader.load()
    return weather_documents