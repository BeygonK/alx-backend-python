#!/usr/bin/env python3
""" Sums the items of
a mixed list
"""


from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """Sums mixed list

    Args:
        mxd_list (List[Union[int, float]]): contains mixed items

    Returns:
        float: final result
    """
    return float(sum(mxd_list))
