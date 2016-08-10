from flask_pymongo import PyMongo
import pymongo


mongodb = PyMongo()


def get_animal_collection():
    animals_collection = mongodb.db['animals']
    animals_collection.create_index([('name', pymongo.ASCENDING)])
    animals_collection.create_index([('type', pymongo.ASCENDING)])
    animals_collection.create_index([('weight', pymongo.ASCENDING)])
    animals_collection.create_index([('height', pymongo.ASCENDING)])
    animals_collection.create_index([
        ('name', pymongo.ASCENDING),
        ('type', pymongo.ASCENDING)
    ], unique=True)
    return animals_collection


def get_farmer_collection():
    return mongodb.db.farmers
