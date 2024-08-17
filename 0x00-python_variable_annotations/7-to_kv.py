#!/usr/bin/env python3
"""module
"""


from typing import Union


def to_kv(k: str, v: Union[int, float]) -> tuple[str, float]:
    """A function to return a tuple

    Args:
        k (str): The first argument
        v (Union[int, float]): The second argument

    Returns:
        tuple: results
    """
    return (k, float(v ** 2))
