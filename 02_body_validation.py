from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Numbers(BaseModel):
    values: List[int]

@app.post("/")
def sum_numbers(data: Numbers):
    total = sum(data.values)
    return {"values": data.values, "sum": total}