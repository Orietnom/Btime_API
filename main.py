from src.service.api_handler import get_weather_data
from src.service.csv_handler import csv_creator
from src.shared.logger import logger

if __name__ == '__main__':

    try:
        rows = get_weather_data()
        csv_creator(rows)
    except Exception as e:
        logger.exception("Failed running Btime_API")
