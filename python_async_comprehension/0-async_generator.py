#!/usr/bin/env python3
"""
Async Generator that yields random floats from 0 to 10
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    This function will loop 10 times.
    For every iteration, it will wait and produce
    a float point between 0 and 10
    Args:
        None
    Returns:
        random numbers between 0-10
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
