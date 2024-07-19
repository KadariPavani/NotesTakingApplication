from pydantic import BaseModel
from typing import List

class NoteBase(BaseModel):
    title: str
    content: str

class NoteCreate(NoteBase):
    pass

class NoteUpdate(NoteBase):
    pass

class Note(NoteBase):
    id: str
    owner_id: str

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "id": "60d21b4667d0d8992e610c85",
                "title": "Sample Note",
                "content": "This is a sample note.",
                "owner_id": "60d21b4667d0d8992e610c84"
            }
        }

class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str

    class Config:
        json_schema_extra = {
            "example": {
                "username": "user1",
                "email": "user1@example.com",
                "password": "strongpassword"
            }
        }

class User(UserBase):
    id: str
    notes: List[Note] = []

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "id": "60d21b4667d0d8992e610c84",
                "username": "user1",
                "email": "user1@example.com",
                "notes": [
                    {
                        "id": "60d21b4667d0d8992e610c85",
                        "title": "Sample Note",
                        "content": "This is a sample note.",
                        "owner_id": "60d21b4667d0d8992e610c84"
                    }
                ]
            }
        }
