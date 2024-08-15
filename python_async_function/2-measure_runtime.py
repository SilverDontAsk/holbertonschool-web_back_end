#!/usr/bin/env python3
"""
Measuring runtime
"""
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the runtime for wait_n
    Args:
        n: number of tasks
        max_delay: max delay for wait_random
    Returns:
        Average runtime per task
    """
    start_clock = time.time()
    await wait_n(n, max_delay)
    total_time = time.time() - start_clock
    return total_time / n
