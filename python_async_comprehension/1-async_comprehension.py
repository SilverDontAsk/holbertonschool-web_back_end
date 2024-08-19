#!/usr/bin/env python3
"""
Async comprehension that collects 10 random floats
"""
async_generator = __import__('0-async_generator').async_generator
import asyncio
from typing import List


async def async_comprehension() -> List[float]:
    """
    Collects 10 random floats asynchronously
    Returns:
        List[float]: list of 10 random float number from
        async_generator
    """
    return [num async for num in async_generator()]