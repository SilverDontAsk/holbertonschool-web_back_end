#!/usr/bin/env python3
"""
Summing a list of floats
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Function to add all the floats of a list
    Args:
        input_list: Expected to be a list that contains floats
    Returns:
        The sum of all floats on the list
    """
    return sum(input_list)
