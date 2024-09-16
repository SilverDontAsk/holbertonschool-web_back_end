#!/usr/bin/env python3
"""
annotationg element length
"""
from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Function to calculate the length of an element
    Args:
        lst: expected to be a list with a sequence
    Returns:
        A tuple with the sequence and its length
    """
    return [(i, len(i)) for i in lst]
