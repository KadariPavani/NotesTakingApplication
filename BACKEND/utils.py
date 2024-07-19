from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from pymongo.collection import Collection
from BACKEND.database import get_database
from BACKEND.schemas import UserCreate
from pymongo import MongoClient
import os

SECRET_KEY = os.getenv("SECRET_KEY", "your_secret_key")
ALGORITHM = "HS256"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Get MongoDB database
def get_db():
    db = get_database()
    try:
        yield db
    finally:
        # MongoDB connections are usually managed by the client itself,
        # so closing might not be necessary here.
        pass

def get_current_user(token: str = Depends(oauth2_scheme), db: Collection = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    # Fetch user from MongoDB
    user = db.users.find_one({"username": username})
    if user is None:
        raise credentials_exception

    # Convert MongoDB object ID to string if needed
    user["_id"] = str(user["_id"])

    return user
