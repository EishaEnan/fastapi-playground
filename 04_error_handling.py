from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float

inventory = {
    "apple": 1.5,
    "banana": 0.99
}

@app.get("/price/{item_name}")
def get_price(item_name: str):
    item_name = item_name.lower()
    if item_name not in inventory:
        raise HTTPException(
            status_code=404,
            detail=f"Item '{item_name}' not found in inventory."
        )
    
    return {"item": item_name, "price": inventory[item_name]}

@app.post("/add-item")
def add_item(item: Item):
    if item.name.lower() in inventory:
        raise HTTPException(
            status_code = 400,
            detail=f"Item '{item.name}' already exists."
        )
    
    inventory[item.name.lower()] = item.price
    return {"message": f"Item '{item.name}' added with price {item.price}"}