"""Generate ref dataframe
"""
from typing import List
from datetime import datetime
import nfl_data_py as nfl

def generate_ref_df(
    # default to past 5 years including current year
    years: List[int] = None
):
    # Default years to the past 5 years, including current year
    if years is None:
        current_year = datetime.today().year
        years = [current_year - i for i in range(5)]

    # Get data from nfl_data_py
    df = nfl.import_officials(
        years=years,
    )

    return df