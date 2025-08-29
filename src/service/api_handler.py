"""API handler for retrieving weather data from the INMET service."""

from dotenv import load_dotenv

import requests
import os

from src.shared.date_to_filter import date_to_filter

load_dotenv()


def get_weather_data():
    """Fetch weather data from INMET for a given date.

        The URL and number of days to subtract are read from environment
        variables. The resulting JSON payload is returned.

        Returns:
            list[dict] | dict: Parsed JSON response with weather data.

        Raises:
            requests.HTTPError: If the request to the API fails.
        """

    # Build the API URL using the configured base URL and date filter.
    url = os.getenv("URL", "https://apitempo.inmet.gov.br/condicao/capitais/{0}")
    complete_url = url.format(date_to_filter(int(os.getenv("DAYS_BEFORE", 0))))

    # Perform the HTTP GET request to the remote service.
    response = requests.get(complete_url)
    try:
        # Raise an exception for any unsuccessful status codes.
        response.raise_for_status()
    except Exception:
        raise

    # Parse the JSON payload and return it.
    json_response = response.json()
    return json_response
