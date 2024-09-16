#!/usr/bin/env python3
"""
Returning tuples from strings and int/floats
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Function to convert elements in a tuple
    Args:
        k: expected to be a string
        v: expected to be either an int or float
    Returns:
        A tuple where 1st element is str and 2nd is int/float
    """
    return (k, float(v ** 2))
