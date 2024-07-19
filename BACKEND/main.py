from fastapi import FastAPI
from BACKEND.ROUTERS import auth, notes

app = FastAPI()

app.include_router(auth.router)
app.include_router(notes.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Note Taking App!"}



