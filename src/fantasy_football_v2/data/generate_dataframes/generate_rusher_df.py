"""Generate rushing data dataframe
"""
from typing import List
from datetime import datetime
import nfl_data_py as nfl

def generate_rusher_df(
    # default to current year
    years: List[int] = None
):
    # Default column list
    columns = [
        'season',
        'week'
    ]

    # Default years to current year