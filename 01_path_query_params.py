from fastapi import FastAPI, Query
from typing import List

app = FastAPI()

# Path Parameter
@app.get("/greet/{name}")
def greetUser(name: str):
    return {"message": f"Hello, {name}"}

# Query parameter
@app.get("/square")
def square_number(x: int):
    return {"x": x, "squared": x * x}

# Multiple path parameters (2 strings)
@app.get("/greet-full/{first}/{last}")
def greet_full_name(first: str, last: str):
    return {"message": f"Hello, {first} {last}"}

# Mix of path and query parameters
@app.get("/math/{a}")
def math_ops(a: int, b: int = 1):
    return {
        "a": a,
        "b": b,
        "sum": a + b,
        "product": a * b
    }

# test - /math/5?b=3

# A query list
@app.get("/multiply")
def multiply(nums: List[int] = Query(...)):
    product = 1
    for n in nums:
        product *= n
    
    return {
        "nums": nums,
        "product": product
    }

# test: /multiply?nums=2&nums=3&nums=4

