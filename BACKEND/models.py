from pydantic import BaseModel
from typing import List, Optional

class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: str

    class Config:
        schema_extra = {
            "example": {
                "username": "john_doe",
                "email": "john@example.com",
                "id": "60c72b2f9b1e8d3f5f5f9b25",
            }
        }

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
        schema_extra = {
            "example": {
                "title": "Sample Note",
                "content": "This is a sample note",
                "id": "60c72b2f9b1e8d3f5f5f9b26",
                "owner_id": "60c72b2f9b1e8d3f5f5f9b25"
            }
        }
