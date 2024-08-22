#!/usr/bin/env python3
"""
Providing stats about Nginx logs
"""


def Nginx_log_provider(mongo_collection):
    """
    Function to provide the nginx logs stored in Mongodb
    Args:
        mongo_collection: pymongo collection object
    Returns:
        Log stats
    """
    all_logs = mongo_collection.count_documents({})
    print(f"{all_logs} logs")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = mongo_collection.count_documents({'method': method})
        print(f"\tmethod {method}: {count}")
    stat_check_count = mongo_collection.count_documents({
        'method': 'GET', 'path': '/status'
    })
    print(f"{stat_check_count} status check")
