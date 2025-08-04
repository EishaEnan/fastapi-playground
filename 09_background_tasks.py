from fastapi import FastAPI, BackgroundTasks
import time

app = FastAPI()

def write_log(username: str):
    # Simulate a slow operation (like writing to file/db)
    time.sleep(2)
    with open("log.txt", "a") as f:
        f.write(f"User '{username}' logged in.\n")

@app.post("/login")
def login(username: str, tasks: BackgroundTasks):
    tasks.add_task(write_log, username)
    return {"message": f"Welcome, {username}! Logging in..."}
