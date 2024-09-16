#!/usr/bin/env python3
"""
Concurrent coroutines
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    This function returns a list of all delays
    Args:
        n: amount of times to count
        max_delay: max timer of the delay
    Returns:
        list of all delays
    """
    tasks = [await wait_random(max_delay) for _ in range(n)]
    delay = []
    for task in tasks:
        delay.append(task)
        for i in range(len(delay) - 1, 0, -1):
            if delay[i] < delay[i - 1]:
                delay[i], delay[i - 1] = delay[i - 1], delay[i]
    return delay
