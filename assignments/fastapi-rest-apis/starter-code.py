from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()


class NoteCreate(BaseModel):
    title: str
    content: str


class Note(NoteCreate):
    id: int


# In-memory storage
notes: List[Note] = []
next_id = 1


@app.get("/notes", response_model=List[Note])
def list_notes():
    return notes


@app.post("/notes", response_model=Note, status_code=201)
def create_note(payload: NoteCreate):
    global next_id
    note = Note(id=next_id, **payload.dict())
    notes.append(note)
    next_id += 1
    return note


@app.get("/notes/{note_id}", response_model=Note)
def get_note(note_id: int):
    for n in notes:
        if n.id == note_id:
            return n
    raise HTTPException(status_code=404, detail="Note not found")


@app.put("/notes/{note_id}", response_model=Note)
def update_note(note_id: int, payload: NoteCreate):
    for i, n in enumerate(notes):
        if n.id == note_id:
            updated = Note(id=note_id, **payload.dict())
            notes[i] = updated
            return updated
    raise HTTPException(status_code=404, detail="Note not found")


@app.delete("/notes/{note_id}", status_code=204)
def delete_note(note_id: int):
    for i, n in enumerate(notes):
        if n.id == note_id:
            notes.pop(i)
            return
    raise HTTPException(status_code=404, detail="Note not found")
