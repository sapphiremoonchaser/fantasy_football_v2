"""Generate rushing data dataframe
"""
from typing import List
from datetime import datetime
import nfl_data_py as nfl

from src.fantasy_football_v2.utilities.time_functions import get_current_season

def generate_rusher_df(
    # default to current year
    years: List[int] = None
):
    # Default column list
    columns = [
        'season',
        'week',
        'player_gsis_id',
        'player_display_name',
        'player_position',
        'team_abbr',
        'efficiency',
        'rush_attempts',
        'rush_yards',
        'avg_rush_yards',
        'rush_touchdowns'
    ]

    # Default years to current year
    if years is None:
        years = get_current_season()

    # Get data from nfl_data_py
    df = nfl.import_ngs_data(
        stat_type='rushing',
        years=years,
    )

    # Filter to regular season games
    df = df[
        df['season_type'] == 'REG'
    ]

    # Drop un-needed columns
    df = df[columns]

    return df