#!/usr/bin/env python3
"""Basic async syntax"""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Basics of async

    Args:
        max_delay (int, optional): max param. Defaults to 10.

    Returns:
        float: float
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay