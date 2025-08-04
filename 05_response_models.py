from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Internal database model (contains everything)
class UserDB(BaseModel):
    id: int
    username: str
    email: str
    password: str # sensitive!
    is_admin: bool

# Public response model (only safe fields)
class UserOut(BaseModel):
    id:int
    username: str
    email: str

# Fake "database"
users = [
    UserDB(id=1, username="alice", email="alice@example.com", password="secret123", is_admin=True),
    UserDB(id=2, username="bob", email="bob@example.com", password="secret321", is_admin=False),
]

@app.get("/users", response_model=List[UserOut])
def get_users():
    return users

@app.get("/users/{user_id}", response_model=UserOut)
def get_user(user_id: int):
    for user in users:
        if user.id == user_id:
            return user
    
    return {"error": "User not found!"}