from pymongo.collection import Collection
from pymongo import MongoClient
from BACKEND.schemas import UserCreate, NoteCreate, NoteUpdate
from BACKEND.security import get_password_hash, verify_password
from bson import ObjectId

# Initialize MongoDB client and database
db = MongoClient().note_taking_app

def get_user_by_username(username: str):
    return db.users.find_one({"username": username})

def create_user(user: UserCreate):
    hashed_password = get_password_hash(user.password)
    user_data = {
        "username": user.username,
        "email": user.email,
        "hashed_password": hashed_password
    }
    result = db.users.insert_one(user_data)
    user_data["_id"] = str(result.inserted_id)
    return user_data

def get_user_by_id(user_id: str):
    # Convert string to ObjectId for querying
    user_object_id = ObjectId(user_id)
    user = db.users.find_one({"_id": user_object_id})
    if user:
        user["_id"] = str(user["_id"])  # Convert ObjectId to string
    return user

def create_user_note(note: NoteCreate, user_id: str):
    note_data = note.dict()
    note_data["owner_id"] = user_id
    result = db.notes.insert_one(note_data)
    note_data["_id"] = str(result.inserted_id)
    return note_data

def get_notes(user_id: str):
    return list(db.notes.find({"owner_id": user_id}))

def update_user_note(note_id: str, note: NoteUpdate):
    # Convert string to ObjectId for querying
    note_object_id = ObjectId(note_id)
    result = db.notes.find_one_and_update(
        {"_id": note_object_id},
        {"$set": note.dict()},
        return_document=True
    )
    if result:
        result["_id"] = str(result["_id"])  # Convert ObjectId to string
    return result

def delete_user_note(note_id: str):
    # Convert string to ObjectId for querying
    note_object_id = ObjectId(note_id)
    result = db.notes.delete_one({"_id": note_object_id})
    return result.deleted_count > 0
