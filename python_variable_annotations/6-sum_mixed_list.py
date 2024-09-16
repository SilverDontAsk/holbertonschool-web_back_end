#!/usr/bin/env python3
"""
Adding together a list containing ints and floats
"""
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """
    Function to add all numbers in the list
    Args:
        mxd_list: List with ints and floats, expected to be a list
    Returns:
        Sum of all numbers in the list
    """
    return sum(mxd_list)
