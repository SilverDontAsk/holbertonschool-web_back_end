#!/usr/bin/env python3
"""
Providing stats about Nginx logs
"""
from pymongo import MongoClient


def Nginx_log_provider():
    """
    Function to provide the nginx logs stored in Mongodb
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_coll = client.logs.nginx
    all_logs = nginx_coll.count_documents({})
    print(f"{all_logs} logs")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = nginx_coll.count_documents({'method': method})
        print(f"\tmethod {method}: {count}")
    stat_check_count = nginx_coll.count_documents({
        'method': 'GET', 'path': '/status'})
    print(f"{stat_check_count} status check")


if __name__ == "__main__":
    Nginx_log_provider()
