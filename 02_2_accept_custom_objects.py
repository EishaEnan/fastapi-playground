from typing import List
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    tags: List[str]

@app.post("/bulk-post")
def upload_posts(posts: List[Post]):
    return {
        "total_posts": len(posts),
        "titles": [p.title for p in posts]
    }