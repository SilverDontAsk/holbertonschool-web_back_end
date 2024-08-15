#!/usr/bin/env python3
"""
Concurrent coroutines
"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    This function returns a list of all delays
    Args:
        n: amount of times to count
        max_delay: max timer of the delay
    Returns:
        list of all delays
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delay = await asyncio.gather(*tasks)
    delay.sort()
    return delay
