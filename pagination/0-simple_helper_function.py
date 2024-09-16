#!/usr/bin/env python3
"""
Simple helper function
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Returns a tuple of the start and end
    based on page and page_size
    Args:
        page: page number
        page_size: items per page
    Returns:
        tuple that contains the start and ending index
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
