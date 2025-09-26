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

from pydantic.v1.errors import cls_kwargs


class Official(BaseModel):
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
        if " " in v:
            raise ValueError(f"The official's id, {v}, should not contain spaces.")

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
        return v.upper()
