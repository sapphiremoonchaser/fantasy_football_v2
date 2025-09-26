"""Official class representing Officials and their position by season.

Classes:
    Official: A Pydantic model representing the official.
"""
from pydantic import (
    BaseModel,
    Field,
    field_validator
)

from datetime import datetime

class Official(BaseModel):
    official_id: str = Field(
        min_length=1,
        frozen=True
    )
    official_name: str = Field(
        min_length=1,
        frozen=True
    )
    season: int = Field(
        ge=2010,
        le=datetime.today().year, # current year
        frozen=True
    )
    position: str = Field(
        min_length=1,
        frozen=True
    )

    # ToDo: Field constraight for "official_id", no spaces
    # 'official_id' should not have spaces

    # ToDo: Field constraint for 'position' to all caps