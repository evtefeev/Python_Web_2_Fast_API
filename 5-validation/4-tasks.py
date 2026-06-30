# Завдання 1.
# Створи модель BookList, яка містить список книг.
# Кожна книга має: title: str, author: str, pages: int (> 10).


from pprint import pprint
from typing import Annotated

from annotated_types import Len
from pydantic import BaseModel, EmailStr, Field, HttpUrl
from pydantic import BaseModel, Field, ValidationError


class Book(BaseModel):
    title: str
    author: str
    pages: int = Field(..., ge=10)


class BooktList(BaseModel):
    books: Annotated[
        list[Book],
        Len(min_length=1),
    ]


books = {
    "books": [
        {"id": 1, "title": "1984", "author": "George Orwell", "pages": 10},
        {"id": 2, "title": "Brave New World", "author": "Aldous Huxley", "pages": 10},
        {
            "id": 3,
            "title": "To Kill a Mockingbird",
            "author": "Harper Lee",
            "pages": 10,
        },
    ]
}

# pprint(BooktList(**books))


# 📌 Перевір:
# Чи всі елементи в списку — валідні.
# Що список не порожній.


# Завдання 2.
# Створи модель Student, де є:
# name: str
# email: EmailStr
# portfolio: HttpUrl
# skills: conlist(str, min_items=2, max_items=5)


class Student(BaseModel):
    name: str
    email: EmailStr
    portfolio: HttpUrl
    skills: Annotated[
        list[str],
        Len(min_length=2, max_length=5),
    ]


# print(
#     Student(
#         name="Nikita",
#         email="nikita@dmail.com",
#         portfolio="https://nikita.com",
#         skills=["python", "fastapi", "flask"],
#     )
# )


# Завдання 3.
# У вас є модель продукту:
class Product(BaseModel):
    name: str = Field(..., min_length=2)
    price: float = Field(..., gt=0)


# 🛠 Створіть об’єкт з невалідними даними:
# name — порожній рядок
# price — від’ємне число

try:
    print(Product(name="nik", price=1))
except ValidationError as e:
    print(e.json())


# ✅ Обробіть ValidationError і надрукуйте її в зручному форматі (наприклад print(e.json()))


# Завдання 4.
# Валідація списку об’єктів
# Є список товарів:
# from typing import List


# class ProductList(BaseModel):
#     items: List[Product]


# 📦 Передайте список, де один із товарів має порожню назву або ціна дорівнює 0.

# ✅ Перевірте, що помилка спрацювала саме для некоректного елементу списку.
