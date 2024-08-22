#!/usr/bin/env python3
"""
Returning list of school with a specfic topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    Function to list schools that
    contain a specific topic
    Args:
        mongo_collection: pymongo collection object
        topic: topic to seach
    Returns:
        schools that contain topic
    """
    cursor = mongo_collection.find({'topics': topic})
    return list(cursor)
