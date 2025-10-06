"""Example of creating ref data models
"""
from src.fantasy_football_v2.data.generate_data_models.generate_ref_model import ref_from_dataframe

refs = ref_from_dataframe()

for ref in refs[:5]:
    print(ref)

x = 1