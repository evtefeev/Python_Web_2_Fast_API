from pydantic import BaseModel, field_validator


class Product(BaseModel):
    name: str
    price: float


    @field_validator('name')
    @classmethod
    def name_must_not_be_empty(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("Назва не може бути порожньою")
        return v



from pydantic import BaseModel, field_validator


class User(BaseModel):
    username: str
    email: str
    age: int


    @field_validator("email")
    @classmethod
    def must_be_gmail(cls, value: str) -> str:
        if not value.endswith("@gmail.com"):
            raise ValueError("Email має бути з домену @gmail.com")
        return value
