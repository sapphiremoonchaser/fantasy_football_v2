"""Generate dataframe with weekly points by player.
"""
from typing import List
from datetime import datetime
import nfl_data_py as nfl

def generate_ref_df(
    # default to past 5 years including current year
    years: List[int]=None,
    columns=None
):
    # Default column list
    if columns is None:
        columns = [
            'game_id',
            'season',
            'week',
            'player_id',
            'player_display_name',
            'position',
            'fantasy_points_ppr'
        ]

    # Default years to the past 5 years, including current year
    if years is None:
        current_year = datetime.today().year
        years = [current_year - i for i in range(5)]

    # Get data from nfl_data_py
    df = nfl.import_weekly_data(
        years=years,
        downcast=True
    )

    # Re-order and keep specific columns
    df = df[columns]

    return df
