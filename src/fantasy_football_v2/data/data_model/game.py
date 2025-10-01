"""Game class representing each game.

Classes:
    Game: A Pydantic model representing the game.
"""
from pydantic import (
    BaseModel,
    Field,
    field_validator
)

from datetime import datetime

class Game(BaseModel):
    """A model representing nfl games.

    Args:
        game_id (str): game_id from nfl.import_schedules,
            im the form seaso_wk_away_home (2025_01_DAL_PHI)
        season (int): the nfl season
        week (int): the nfl week
        referee (str): the name of the ref
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
    referee: str = Field(
        min_length=1,
        frozen=True
    )