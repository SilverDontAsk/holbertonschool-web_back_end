#!/usr/bin/env python3
"""
Concurrent coroutines
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n, max_delay):
    """
    This function returns a list of all delays
    Args:
        n: amount of times to count
        max_delay: max timer of the delay
    Returns:
        list of all delays
    """
    delay = []
    tasks = [wait_random(max_delay) for _ in range(n)]
    for task in asyncio.as_completed(tasks):
        delay.append(await task)
    return delay
