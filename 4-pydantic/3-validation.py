from pydantic import BaseModel, EmailStr, ValidationError, field_validator
from pydantic import Field
from fastapi import FastAPI
import uvicorn
class Item(BaseModel):
    name: str = Field(..., min_length=3, description="Назва товару")
    price: float = Field(..., gt=0, description="Ціна повинна бути більше нуля")
    description: str | None = None



class UserInput(BaseModel):
    name: str = Field(..., min_length=3, max_length=25, description="User Name")
    email: EmailStr
    age: int = Field(..., gt=14, lt=100, description="Age must be between 14 and 100")

    @field_validator('email')
    @classmethod
    def email_from_trust_domain(cls, v: str) -> str:
        trusted_domains = ["gmail.com"]
        if v.split("@")[1] not in trusted_domains:
            raise ValueError("email invalid")
        return v
    
app=FastAPI()

@app.post("/userinput/")
def userinput(userinput:UserInput):
    return {"input":userinput}


try:
    user = UserInput(
        name="Alex",
        email="alexe@agmail.com",
        age="13"  
    )
    print(user.model_dump())
except ValidationError as e:
    print(e.json())

uvicorn.run(app)









# class Item(BaseModel):
# 			name: str = Field(..., example="Coffee", description="The name of the item")
# 			description: str = Field(None, example="A hot, stimulating drink", description="A detailed description of the item")
# 			price: float = Field(..., gt=0, description="The price of the item must be greater than zero")
# 			tax: float = None