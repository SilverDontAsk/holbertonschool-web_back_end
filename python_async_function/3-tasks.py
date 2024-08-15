#!/usr/bin/env python3
"""
Returning a task
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    creates an asyncio task around wait_random
    Args:
        max_delay: max delay for wait_random
    Returns:
        an Asyncio.Task object
    """
    return asyncio.create_task(wait_random(max_delay))
