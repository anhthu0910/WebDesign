from fastapi import FastAPI, Query, HTTPException
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel


class ItemCreate(BaseModel):
    name: str
    price: float
    in_stock: bool = True

class ItemPublic(BaseModel):
    id: int
    name: str
    price: float

_items: list[ItemPublic] = []
_next_id: int = 1

app = FastAPI()
app.mount("/static", StaticFiles(directory="../frontend"), name="static")

def _find(item_id: int) -> ItemPublic | None:
    for it in _items:
        if it.id == item_id:
            return it
    return None

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/items/me")
def read_me():
    return "Welcome"

# Get item by ID
@app.get("/items/{item_id}")
def read_item(item_id: int):
    item = _find(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail=f"Item with ID {item_id} not found")
    return item

# GET ITEMS
@app.get("/items")
def read_items(
    skip: int = Query(0, ge=0, description="Number of items to skip"),
    limit: int = Query(10, ge=1, description="Maximum number of items to return"),
    q: str = Query(None, description="Query string for searching items")
):
    return _items[skip: skip + limit]

# CREATE AN ITEM
@app.post("/items", response_model=ItemPublic, status_code=201)
def create_item(data: ItemCreate):
    global _next_id
    newItem = ItemPublic(id=_next_id, name=data.name, price=data.price)
    _items.append(newItem)
    _next_id += 1
    return newItem

# UPDATE AN ITEM
@app.put("/items", response_model=ItemPublic)
def update_item(item_id: int, data: ItemPublic):
    item = _find(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail=f"Item with ID {item_id} not found")
    
    # update
    updateValue = ItemPublic(id=item.id, name=data.name, price=data.price)
    index = _items.index(item)
    _items[index] = updateValue
    
    return updateValue

# DELETE AN ITEM
@app.delete("/items")
def delete_item(item_id: int):
    item = _find(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail=f"Item with ID {item_id} not found")
    
    _items.remove(item)
    return {"message": f"Item with ID {item_id} deleted successfully"}