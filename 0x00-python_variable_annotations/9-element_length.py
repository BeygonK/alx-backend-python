#!/usr/bin/env python3
"""Duck typing"""


from typing import List, Tuple, Iterable, Sequence

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """summary

    Args:
        lst (List[str]): description

    Returns:
        List[Tuple[str, int]]: description
    """
    return [(i, len(i)) for i in lst]
