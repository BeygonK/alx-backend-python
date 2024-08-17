#!/usr/bin/env python3
"""multiplier"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Multiplier

    Args:
        multiplier (float): The first argument

    Returns:
        Callable[[float], float]: result
    """
    def multiplier_function(value: float) -> float:
        return value * multiplier

    return multiplier_function
