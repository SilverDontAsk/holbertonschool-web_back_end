#!/usr/bin/env python3
"""
listing all docs in a mongodb collection
"""


def list_all(mongo_collection):
    """
    Function to list all docs in a MongoDB collection
    Args:
        mongo_collection: pymongo collection object
    Returns:
        list: list of docs in the collection
    """
    return list(mongo_collection.find())
