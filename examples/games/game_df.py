"""Example of creating the game dataframe
"""
from src.fantasy_football_v2.data.generate_dataframes.generate_game_df import generate_game_df

# Dataframe of games
game_df = generate_game_df(
    years=[2021, 2022, 2023, 2024, 2025]
).reindex()

x = 1