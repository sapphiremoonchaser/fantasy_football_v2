"""Create ref data model
"""
from src.fantasy_football_v2.data.generate_dataframes.generate_ref_df import generate_ref_df
from src.fantasy_football_v2.data.data_model.ref import Ref

from typing import List


def ref_from_dataframe() -> List[Ref]:
    """This function calls generate_ref_df function
    """
    # Create the ref dataframe
    ref_df = generate_ref_df()

    # iterate of rows to create individual ref data models
    refs = [Ref(**record) for record in ref_df.to_dict(orient='records')]

    return refs