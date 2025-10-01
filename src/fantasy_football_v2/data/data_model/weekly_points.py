"""WeeklyPoints class representing weekly fantasy ppr points by players
"""
from pydantic import (
    BaseModel,
    Field,
    field_validator
)

from datetime import datetime

class WeeklyPoints(BaseModel):
    """A model representing weekly fantasy ppr point at the player level

    Args:
        game_id (str): game_id from nfl.import_schedules
        season (int): nfl season
        week (int): nfl week
        player_id (str): player id from nfl.import_weekly_stats
        player_display_name (str): ex: Aaron Rogers
        position (str): abbreviation of the position
        fantasy_points_ppr (float): fantasy point in ppr leagues
    """
    game_id: (str) = Field(
        min_length=14,
        max_length=14,
        frozen=True
    )
    season: int = Field(
        ge=2010,
        le=datetime.today().year, # current year
        frozen=True
    )
    week: int = Field(
        ge=0,
        le=30,
        frozen=True
    )
    player_id: str = Field(
        min_length=1,
        frozen=True
    )
    player_display_name: str = Field(
        min_length=1,
        frozen=True
    )
    position: str = Field(
        min_length=1,
        max_length=3,
        frozen=True
    )
    fantasy_points_ppr: float = Field(
        frozen=True,
    )