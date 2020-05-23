import requests
import logging

import settings

log = logging.getLogger(__name__)


class Weather:

    def __init__(self, latitude=None, longitude=None, city=None):
        self.latitude = latitude
        self.longitude = longitude
        self.city = city

    def get_weather(self):
        weather_url = "https://api.worldweatheronline.com/premium/v1/weather.ashx"
        params = {
            "key": settings.API_WEATHER,
            "q": f"{self.latitude}, {self.longitude}",
            "format": "json",
            "num_of_days": "1",
            "lang": "ru",
        }
        logging.info(f"Params = {params['q']}")
        try:
            result = requests.get(weather_url, params=params)
            result.raise_for_status()
        except requests.RequestException as e:
            logging.info(f"Exception = {e}")
            return False
        else:
            try:
                weather = result.json()
                if "data" in weather:
                    if "current_condition" in weather["data"]:
                        try:
                            return weather["data"]["current_condition"][0]
                        except(IndexError, TypeError):
                            return False
            except ValueError as e:
                logging.info(f"Exception = {e}")
                return False
        return False
