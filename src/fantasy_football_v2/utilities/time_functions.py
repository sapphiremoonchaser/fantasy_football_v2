"""This file contains functions that deal with time
"""
from datetime import datetime

def get_current_season(

):
    # Get the current month
    current_month = datetime.today().month

    # If end of year then current year
    # Season restarts in March
    if current_month in range(3, 13): # Last number not inclusive
        season = datetime.today().year
    else:
        season = datetime.today().year - 1

    return season