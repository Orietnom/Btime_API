from dotenv import load_dotenv

import requests
import os

from src.shared.date_to_filter import date_to_filter

load_dotenv()


def get_weather_data():
    url = os.getenv("URL", "https://apitempo.inmet.gov.br/condicao/capitais/{0}")
    complete_url = url.format(date_to_filter(int(os.getenv("DAYS_BEFORE", 0))))
    response = requests.get(complete_url)
    try:
        response.raise_for_status()
    except Exception:
        raise

    json_response = response.json()
    return json_response
