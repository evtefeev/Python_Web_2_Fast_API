from pydantic import BaseModel, ValidationError, Field
from typing import List


class Item(BaseModel):
    name: str
    description: str
    price: float = Field()


class ItemList(BaseModel):
    items: List[Item]


data_to_validate = {
    "items": [
        {"name": "Apple", "description": "Fruit", "price": 0.5},
        {"name": "Orange", "description": "Fruit", "price": 0.8},
        {"name": "Banana", "description": "Fruit", "price": -1},
    ]
}


try:
    validated = ItemList(**data_to_validate)
    print(validated)
except ValidationError as e:
    print(e.json())
