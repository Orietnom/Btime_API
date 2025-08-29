"""Utilities for writing weather data to CSV files."""

from pathlib import Path
from typing import List, Dict
from datetime import datetime

import csv

from src.shared.logger import logger

BASE_DIR = Path(__file__).resolve().parent.parent.parent
OUTPUT_DIR = BASE_DIR / "output"


def csv_creator(rows: List[Dict]):
    """Create a CSV file containing the provided weather data.

        Args:
            rows: A list of dictionaries representing rows of weather data.
        """

    logger.info("Creating a CSV with de weather data")
    # Determine column headers from the first dictionary.
    fields = (rows[0].keys())

    # Use current timestamp to create a unique filename.
    today = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Make sure the output directory exists before writing the file.
    OUTPUT_DIR.mkdir(exist_ok=True)

    file_name = OUTPUT_DIR / f"inmet_{today}.csv"
    with open(file_name, 'w', newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields, delimiter="|")
        # Write the header row followed by the data rows.
        w.writeheader()
        # Write the data rows.
        w.writerows(rows)

    logger.success("CSV created with success")