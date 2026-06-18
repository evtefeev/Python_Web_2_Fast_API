from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, field_validator, ValidationError


app = FastAPI()


class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None


    @field_validator('price')
    def price_must_be_positive(cls, value):
        if value <= 0:
            raise ValueError('Price must be positive')
        return value


@app.post("/items/")
def create_item(item: Item):
    try:
        return item
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=e.errors())
