from pydantic import BaseModel, ValidationError, field_validator


class Username(str):
    pass


class User(BaseModel):
    name: Username


    @field_validator('name')
    @classmethod
    def name_must_contain_space(cls, v: str) -> str:
        if ' ' not in v:
            raise ValueError('Username повинен містити пробіл')
        return v.title()


try:
    User(name='johndoe')
except ValidationError as e:
    print(e)
