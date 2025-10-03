"""Generate dataframe with weekly points by player.
"""
from typing import List
from datetime import datetime
import nfl_data_py as nfl

from src.fantasy_football_v2.data.generate_dataframes.generate_game_df import generate_game_df

def generate_weekly_points_df(
    # default to past 5 years including current year
    years: List[int]=None
):
    # Default years to the past 5 years, including current year
    if years is None:
        current_year = datetime.today().year - 1
        years = [current_year - i for i in range(5)]

    # Get data from nfl_data_py
    df = nfl.import_weekly_data(
        years=years,
        downcast=True
    )

    # Filter the regular season games
    df = df[
        df["season_type"] == 'REG'
    ]

    # Columns to keep
    columns = [
        'season',
        'week',
        'player_id',
        'player_display_name',
        'recent_team',
        'position',
        'fantasy_points_ppr'
    ]
    df = df[columns]

    # Generate game dataframe to match to so we can get game_id
    df2 = generate_game_df()

    # Explode teams from df2 to make 2 rows per game (one for each team0
    df2 = df2.explode("teams")

    # Join on season, week, and team/recent_team
    df = df.merge(
        df2[['season', 'week', 'teams', 'game_id']],
        left_on=['season', 'week', 'recent_team'],
        right_on=['season', 'week', 'teams'],
        how='left'
    ).drop(columns=['teams'])

    return df
