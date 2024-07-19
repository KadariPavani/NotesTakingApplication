



from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..schemas import Note, NoteCreate, NoteUpdate
from ..crud import get_notes, create_user_note, update_user_note, delete_user_note
from ..utils import get_db, get_current_user
from ..models import User

router = APIRouter()

@router.get("/notes", response_model=list[Note])
def read_notes(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return get_notes(db, current_user.id)

@router.post("/notes", response_model=Note)
def create_note(note: NoteCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return create_user_note(db, note, current_user.id)

@router.put("/notes/{note_id}", response_model=Note)
def update_note(note_id: int, note: NoteUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_note = update_user_note(db, note_id, note)
    if db_note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    return db_note

@router.delete("/notes/{note_id}", response_model=dict)
def delete_note(note_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    success = delete_user_note(db, note_id)
    if not success:
        raise HTTPException(status_code=404, detail="Note not found")
    return {"detail": "Note deleted successfully"}
