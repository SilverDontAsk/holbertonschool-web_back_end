#!/usr/bin/env python3
"""
inserting a doc into a mongoDB collection
with pymongo
"""


def insert_school(mongo_collection, **kwargs):
    """
    Function to insert a doc into a collection
    Args:
        mongo_collection: pymongo collection object
        **kwargs: fields in the new doc
    Returns:
        str: _id of new doc
    """
    res = mongo_collection.insert_one(kwargs)
    return res.inserted_id
