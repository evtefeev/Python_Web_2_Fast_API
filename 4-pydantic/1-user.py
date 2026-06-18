from fastapi import FastAPI
from pydantic import BaseModel
from typing import List


# user = {
#     "username": "john_doe",
#     "email": "john.doe@example.com",
#     "age": 30,
#     "interests": ["programming", "books", "travel"],
# }


app = FastAPI()


# Модель користувача
class User(BaseModel):
    username: str
    email: str
    age: int
    interests: List[str]


@app.post("/users/")
async def create_user(user: User):
    # FastAPI автоматично конвертує JSON-запит у екземпляр User
    return {"message": "Користувач створений!", "user": user}
