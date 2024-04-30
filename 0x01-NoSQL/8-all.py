#!/usr/bin/env python3

"""
function that lists all documents in a collection:

    Prototype: def list_all(mongo_collection):
"""
def list_all(mongo_collection):
    document = mongo_collection.find()
    return(mongo_collection)
