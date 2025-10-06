"""Generate ref dataframe
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
            'official_id',
            'name',
            'season',
            'off_pos'
        ]

    # Default years to the past 5 years, including current year
    if years is None:
        current_year = datetime.today().year
        years = [current_year - i for i in range(5)]

    # Get data from nfl_data_py
    df = nfl.import_officials(
        years=years
    )

    # Re-order and keep specific columns
    df = df[columns]

    # drop duplicates (originally this was by game, so duplicates occur when that column was dropped)
    df = df.drop_duplicates()

    # Get a unique list of refs for the current year
    current_refs = df.loc[
        df['season'] == datetime.today().year,
        "official_id"
    ].unique()

    # Filter df to include only current refs
    df = df[
        df["official_id"].isin(current_refs)
    ]

    # Rename columns
    df = df.rename(
        columns={
            "official_id": "id",
            "off_pos": "position"
        }
    )

    return df