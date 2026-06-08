from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List

app = FastAPI()


class ItemCreate(BaseModel):
    name: str = Field(..., min_length=1)
    description: str = ""


class Item(ItemCreate):
    id: int


items: List[Item] = []
next_id = 1


@app.post("/items", response_model=Item, status_code=201)
def create_item(payload: ItemCreate):
    global next_id
    item = Item(id=next_id, **payload.dict())
    items.append(item)
    next_id += 1
    return item


@app.get("/items", response_model=List[Item])
def list_items():
    return items
