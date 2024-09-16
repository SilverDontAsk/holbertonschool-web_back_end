#!/usr/bin/env python3
"""
Measuring the runtime of parellel executions
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measures the runtime of async_comprehension
    four times in parallel.
    Returns:
        float: total runtime
    """
    start_time = time.time()
    progress = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*progress)
    end_time = time.time()
    return end_time - start_time
