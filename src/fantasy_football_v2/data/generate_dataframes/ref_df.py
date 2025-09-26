"""Generate ref dataframe
"""
from typing import List
from datetime import datetime
import nfl_data_py as nfl

def generate_ref_df(
    # default to past 5 years including current year
    years: List[int] = [datetime.today().year - i for i in range(5)]
):
    # Get data from nfl_data_py
    df = nfl.import_officials(
        years=years,
    )

    return df