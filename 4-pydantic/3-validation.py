from pydantic import BaseModel, EmailStr, ValidationError


class UserInput(BaseModel):
    name: str
    email: EmailStr
    age: int


try:
    user = UserInput(
        name="Alex",
        email="alex@example.com",
        age="22"  # буде автоматично перетворено на int
    )
    print(user.dict())
except ValidationError as e:
    print(e.json())



from pydantic import BaseModel, Field


class Item(BaseModel):
    name: str = Field(..., min_length=3, description="Назва товару")
    price: float = Field(..., gt=0, description="Ціна повинна бути більше нуля")
    description: str | None = None



class Item(BaseModel):
			name: str = Field(..., example="Coffee", description="The name of the item")
			description: str = Field(None, example="A hot, stimulating drink", description="A detailed description of the item")
			price: float = Field(..., gt=0, description="The price of the item must be greater than zero")
			tax: float = None