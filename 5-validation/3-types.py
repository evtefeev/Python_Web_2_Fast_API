from pydantic import BaseModel, Field, EmailStr, HttpUrl
from typing import Optional


class User(BaseModel):
    name: str
    email: EmailStr
    website: HttpUrl
    age: Optional[int] = Field(None, ge=13, le=90)
    friends: Optional[int] = 0



# Валідні дані
user = User(name="John", email="john@example.com", website="https://john.com", age=25)


# Невалідний вік
User(name="Jane", email="jane@example.com", website="https://jane.com", age=13)


# Невалідний сайт
User(name="Bob", email="bob@example.com", website="http://invalid.rgergregr", age=20)