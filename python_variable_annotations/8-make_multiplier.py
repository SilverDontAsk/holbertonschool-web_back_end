#!/usr/bin/env python3
"""
Multiplying a float with a multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    this function will return a callable that takes float
    and returns a float
    Args:
        multiplier: number which will be multiplied
        in a seperate function
    Returns:
        Returns the result of the multiply function
    """
    def multiply(multiple: float) -> float:
        """
        This function multiplies the called multiple
        with the multiplier
        Args:
            multiple: number to be multiplied by
        Returns:
            multiplication of multiplier and a multiple
        """
        return multiple * multiplier
    return multiply
