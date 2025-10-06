"""Example of creating the weekly points df
"""
from src.fantasy_football_v2.data.generate_dataframes.generate_weekly_points_df import generate_weekly_points_df

# Dataframe with weekly points
points_df = generate_weekly_points_df([2024]).reindex()

x = 1