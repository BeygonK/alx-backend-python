#!/usr/bin/env python3
"""Duck typing"""


from typing import List, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """summary

    Args:
        lst (List[str]): description

    Returns:
        List[Tuple[str, int]]: description
    """
    return [(i, len(i)) for i in lst]
