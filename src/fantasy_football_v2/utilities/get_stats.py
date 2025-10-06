"""Get generic stats like min, max, mean, median, and max
"""
from typing import List

import pandas as pd
from IPython.core.display_functions import display


def get_summary_stats(
        df: pd.DataFrame,
        metric: str,
        identifiers: List[str]
):
    """This function takes a dataframe and gets the row with the min value of a specified metric,
        the row with the max value of a specified metric, and calculates the mean and median of the
        specified metric. It then builds a summary dataframe and includes the specified identifiers
        for the min and max rows.

    :param df:
    :param metric:
    :param identifiers:
    :return:
    """
    # Get the row with the metric minimum
    min_row: pd.Series
    min_row = df.loc[
        df[metric].idxmin()
    ]

    # Get the row with the metric maximum
    max_row: pd.Series
    max_row = df.loc[
        df[metric].idxmax()
    ]

    # Get the mean (just the stat)
    mean_value: float
    mean_value = df[metric].mean()

    # Get the median (just the stat)
    median_value: float
    median_value = df[metric].median()

    # Build summary table
    summary = pd.DataFrame({
        'Statistic': ['Min', 'Mean', 'Median', 'Max'],
        identifiers[0]: [
            min_row[identifiers[0]],
            '-',
            '-',
            max_row[identifiers[0]]
        ],
        identifiers[1]: [
            min_row[identifiers[1]],
            '-',
            '-',
            max_row[identifiers[1]]
        ],
        metric: [
            round(min_row[metric], 2),
            round(mean_value, 2),
            round(median_value, 2),
            round(max_row[metric], 2)
        ]
    })

    return display(
        summary.style.set_caption(f'{metric}')
        .hide(axis="index")
    )
