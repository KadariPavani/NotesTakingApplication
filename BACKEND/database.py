from pymongo import MongoClient

# Initialize MongoDB client and database
client = MongoClient('mongodb://localhost:27017/')
db = client.note_taking_app

def get_database():
    return db
