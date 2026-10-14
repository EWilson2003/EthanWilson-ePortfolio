"""
CS 340 Animal Shelter CRUD baseline reconstructed for the CS 499 before/after comparison.
The historical source file was not available in the supplied CS 499 package.
"""

from pymongo import MongoClient


class AnimalShelter:
    def __init__(self, username, password):
        self.client = MongoClient(
            "mongodb://%s:%s@localhost:27017/?authSource=AAC"
            % (username, password)
        )
        self.database = self.client["AAC"]
        self.collection = self.database["animals"]

    def create(self, data):
        if data is not None:
            self.collection.insert_one(data)
            return True
        return False

    def read(self, query):
        if query is None:
            query = {}
        return list(self.collection.find(query))

    def update(self, query, data):
        result = self.collection.update_many(query, {"$set": data})
        return result.modified_count

    def delete(self, query):
        result = self.collection.delete_many(query)
        return result.deleted_count
