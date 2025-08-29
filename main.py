from src.service.api_handler import get_weather_data
from src.service.csv_handler import csv_creator

if __name__ == '__main__':
    rows = get_weather_data()
    csv_creator(rows)
