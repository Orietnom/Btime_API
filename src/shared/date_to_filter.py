"""Helper for generating dates used in API filtering."""

from datetime import datetime, timedelta


def date_to_filter(days_before: int = 0):
    """Return a formatted date string for a given number of days ago.

        Args:
            days_before: Number of days to subtract from today. Defaults to 0.

        Returns:
            str: Date formatted as ``YYYY-MM-DD``.
        """

    # Compute the target date by subtracting the specified days.
    formatted_date = datetime.now() - timedelta(days=days_before)
    # Return the date in the format expected by the API.
    return formatted_date.strftime("%Y-%m-%d")
