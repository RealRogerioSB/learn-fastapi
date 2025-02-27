from enum import Enum

import uvicorn
from fastapi import FastAPI, HTTPException, Path, Query
from pydantic import BaseModel, Field

app = FastAPI(
    title="Arjan's Handyman Emporium",
    description="Arjan does not only code but also helps you fix things. **See what's in stock!**",
    version="0.1.0",
)


class Category(Enum):
    """Category of an item"""
    TOOLS = "tools"
    CONSUMABLES = "consumables"


class Item(BaseModel):
    """Representation of an item in the system."""
    name: str = Field(description="Name of the item.")
    price: float = Field(description="Price of the item in Euro.")
    count: int = Field(description="Amount of instances of this item in stock.")
    id: int = Field(description="Unique integer that specifies this item.")
    category: Category = Field(default=Category.TOOLS, description="Category this item belongs to.")


items = {
    1: Item(name="Hammer", price=9.99, count=20, id=1, category=Category.TOOLS),
    2: Item(name="Pliers", price=5.99, count=60, id=2, category=Category.TOOLS),
    3: Item(name="Nails", price=1.99, count=100, id=3, category=Category.CONSUMABLES),
}


@app.get("/items")
def index() -> dict[str, dict[int, Item]]:
    return {"items": items}


@app.get("/item/{item_id}")
def query_item_by_id(item_id: int) -> Item:
    if item_id not in items:
        raise HTTPException(status_code=404, detail=f"Item with {item_id=} does not exist.")

    return items[item_id]


@app.get("/item")
def query_item_by_parameters(
    name: str | None = None,
    price: float | None = None,
    count: int | None = None,
    category: Category | None = None,
) -> dict[str, dict[str, str | int | float | Category | None] | list[Item]]:
    def check_item(item: Item):
        """Check if the item matches the query arguments from the outer scope."""
        return all((
            name is None or item.name == name,
            price is None or item.price == price,
            count is None or item.count == count,
            category is None or item.category is category,
        ))

    return {
        "query": {"name": name, "price": price, "count": count, "category": category},
        "selection": [item for item in items.values() if check_item(item)],
    }


@app.post("/item")
def add_item(item: Item) -> dict[str, Item]:
    if item.id in items:
        raise HTTPException(status_code=400, detail=f"Item with {item.id=} already exists.")

    items[item.id] = item

    return {"added": item}


@app.put(
    "/item/{item_id}",
    responses={
         404: {"description": "Item not found"},
         400: {"description": "No arguments specified"}
    },
)
def update(
    item_id: int = Path(title="Item ID", description="Unique integer that specifies an item.", ge=0),
    name: str | None = Query(
        title="Name",
        description="New name of the item.",
        default=None,
        min_length=1,
        max_length=8,
    ),
    price: float | None = Query(
        title="Price",
        description="New price of the item in Euro.",
        default=None,
        gt=0.0,
    ),
    count: int | None = Query(
        title="Count",
        description="New amount of instances of this item in stock.",
        default=None,
        ge=0,
    ),
):
    if item_id not in items:
        raise HTTPException(status_code=404, detail=f"Item with {item_id=} does not exist.")

    if all(info is None for info in (name, price, count)):
        raise HTTPException(status_code=400, detail="No parameters provided for update.")

    item = items[item_id]
    item.name = name or item.name
    item.price = price or item.price
    item.count = count or item.count

    return {"updated": item}


@app.delete("/item/{item_id}")
def delete_item(item_id: int) -> dict[str, Item]:
    if item_id not in items:
        raise HTTPException(status_code=404, detail=f"Item with {item_id=} does not exist.")

    item = items.pop(item_id)

    return {"deleted": item}


if __name__ == '__main__':
    uvicorn.run(app="arjan_fastapi:app", port=5000)
