#!/usr/bin/env python3
"""
Async Generator
"""
import asyncio
import random


async def async_generator():
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
