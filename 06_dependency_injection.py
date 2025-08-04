from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# Dummy users (username: role)
fake_users = {
    "alice": "admin",
    "bob": "user",
}

# Dependency function: extract user and check if they exist
def get_current_user(username: Optional[str] = None):
    if username is None or username not in fake_users:
        raise HTTPException(status_code=401, detail="Invalid or missing user")
    return {"username": username, "role": fake_users[username]}

@app.get("/whoami")
def who_am_i(user=Depends(get_current_user)):
    return {
        "message": f"Hello {user['username']}, you are a(n) {user["role"]}."
    }

@app.get("/admin-only")
def admin_endpoint(user=Depends(get_current_user)):
    if user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Admins only!")
    return {"message": f"Welcome, admin {user["username"]}!"}


