"""Generate game dataframe
"""
from typing import List
from datetime import datetime
import nfl_data_py as nfl

def generate_game_df(
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
            'game_type',
            'referee'
        ]

    # Default years to the past 5 years, including current year
    if years is None:
        current_year = datetime.today().year
        years = [current_year - i for i in range(5)]

    # Get data from nfl_data_py
    df = nfl.import_schedules(
        years=years
    )

    # Filter to regular season games
    df = df[
        df['game_type'] == 'REG'
    ]

    # Drop 'game_type' column
    df = df.drop(['game_type'], axis=1)

    #Combine 'away_team' and 'home_team' into one column with type List
    df['teams'] = df[
        ['away_team', 'home_team']].values.tolist()

    df = df[[
        'game_id',
        'season',
        'week',
        'teams',
        'referee'
    ]]

    return df