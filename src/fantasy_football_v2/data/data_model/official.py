"""Ref class representing Ref's and their position by season. The goal is to get a list of ref's and their position by
    season.

Classes:
    Ref: A Pydantic model representing the ref. A validator has been added to make sure id does not have any
        spaces and a validator to make sure that position is all caps.
"""
from pydantic import (
    BaseModel,
    Field,
    field_validator
)

from datetime import datetime


class Ref(BaseModel):
    """A model representing nfl refs.

    Args:
        id (str): the ref_id from nfl.import_officials
        name(str): the ref's name
        season(int): the nfl season
        position(str): The abbreviated position of the ref
    """
    id: str = Field(
        min_length=1,
        frozen=True
    )
    name: str = Field(
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

    # 'official_id' should not have spaces
    @field_validator(
        'id',
        mode='before'
    )
    def check_id(
            cls,
            v: str
    ) -> str:
        """Validate that id does not have any spaces. This helps keep me from getting name and id mixed up."""
        if " " in v:
            raise ValueError(f"The ref's id, {v}, should not contain spaces.")

        return v

    # 'position' to all caps
    @field_validator(
        'position',
        mode='before'
    )
    def uppercase_position(
            cls,
            v: str
    ) -> str:
        """Uppercase position for consistency."""
        return v.upper()
