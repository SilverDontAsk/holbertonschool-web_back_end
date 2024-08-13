#!/usr/bin/env python3
"""
annotationg element length
"""
from typing import List, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """
    Function to calculate the length of an element
    Args:
        lst: expected to be a list with a string
    Returns:
        A tuple with the str and its length
    """
    return [(i, len(i)) for i in lst]