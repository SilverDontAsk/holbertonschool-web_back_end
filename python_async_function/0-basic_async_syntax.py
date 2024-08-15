#!/usr/bin/env python3
"""
Asynchronous Routine
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    This function generates a random float from 0
    to the max delay, in this case, 10.
    Then it returns the delay time.
    Args:
        max_delay: max delay number, usually an int.
    Returns:
        delay time of the function.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay