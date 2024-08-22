#!/usr/bin/env python3
"""
changing topics of a school doc based on name
"""


def update_topics(mongo_collection, name, topics):
    """
    Function to update topics of a school
    document based on the name
    Args:
        mongo_collection: pymongo collection object
        name: school name to update
        topics: list of topics approached in school
    Returns:
        number of docs modified
    """
    res = mongo_collection.update_many(
        { 'name': name },
        { '$set': { 'topics': topics } }
    )
    return res.modified_count
