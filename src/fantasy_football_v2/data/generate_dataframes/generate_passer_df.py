"""Generate passing data dataframe
"""
from typing import List
from datetime import datetime
import nfl_data_py as nfl

from src.fantasy_football_v2.utilities.time_functions import get_current_season

def generate_passer_df(
    # default to current year
    years: List[int]=None
):
    # Default column list
    columns = [
        'season',
        'week',
        'player_gsis_id',
        'player_display_name',
        'player_position', # Filter to 'QB'
        'team_abbr',
        'avg_time_to_throw',
        'aggressiveness',
        'max_completed_air_distance',
        'attempts',
        'pass_yards',
        'pass_touchdowns',
        'interceptions',
        'passer_rating',
        'completions',
        'completion_percentage',
        'avg_air_distance',
        'max_air_distance'
    ]

    # Default years to current year
    if years is None:
        years = get_current_season()

    # Get data frame from nfl_data_py
    df = nfl.import_ngs_data(
        stat_type='passing',
        years=years,
    )

    # Filter to regular season games
    df = df[
        df['season_type'] == 'REG'
    ]

    # Drop un-needed columns
    df = df[columns]

    return df