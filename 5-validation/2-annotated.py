from typing import Annotated
from pydantic import BaseModel, ValidationError, StringConstraints
from annotated_types import Len


class ProductList(BaseModel):
    product_names: Annotated[
        list[Annotated[str, StringConstraints(min_length=2, max_length=10)]],
        Len(min_length=2, max_length=5),
    ]


data = {"product_names": ["Apple", "Banana", "Cherry"]}

valid = ProductList(**data)

# invalid = {"product_names": ["A", "VeryLongProductNameExceedingLimit", "Z"]}
items = {
    "product_names": [
        "Apple",
        "Banana",
        "Cherry",
        "Apple",
        "Banana",
        "Cherry",
        "Apple",
        "Banana",
        "Cherry",
    ]
}

def limit(items, limit):
    res = {}
    for key, value in items.items():
        res[key] = value[:limit]
    return res



items = limit(items, 5)


try:
    print(ProductList(**items))
except ValidationError as e:
    print(e.json(indent=2))
