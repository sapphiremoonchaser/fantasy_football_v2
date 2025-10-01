"""Example of creating the ref's dataframe
"""
from src.fantasy_football_v2.data.generate_dataframes.generate_ref_df import generate_ref_df

# Dataframe of current refs
ref_df = generate_ref_df(
    years=[2021, 2022, 2023, 2024, 2025]
).reindex()

x = 1