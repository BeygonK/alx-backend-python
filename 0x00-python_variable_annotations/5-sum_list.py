#!/usr/bin/env python3
"""Module adds items in list

"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """Accepts List as param
    and returns sum

    Args:
        input_list (List[float]): Contains float

    Returns:
        float: sum of items in list
    """
    return sum(input_list)
