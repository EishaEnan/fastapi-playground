from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()

class User(BaseModel):
    username: str
    email: EmailStr
    age: int

@app.post("/signup")
def signup(user: User):
    return {
        "message": f"User '{user.username}' registered successfully!",
        "email": user.email,
        "age": user.age
    }