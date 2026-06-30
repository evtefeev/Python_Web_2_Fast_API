from fastapi import FastAPI
from pydantic import BaseModel
import json

import uvicorn


app = FastAPI()


class User(BaseModel):
    name: str
    age: int
    isEmployed: bool
    skills: list


@app.post("/user/")
def create_user(user: User):
    return user





data = {
    "name": "John",
    "age": 30,
    "skills": ["Python", "FastAPI"]
}


json_data = json.dumps(data, indent=2)
print(json_data)


if __name__ =="__main__":
    uvicorn.run(app)