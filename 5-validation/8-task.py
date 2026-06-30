# Завдання 1. Валідація параметрів у маршруті

# Створи ендпойнт /users/{user_id}, який:

# Отримує user_id як ціле число з обмеженням ge=1.
# Приймає обов'язковий заголовок X-Client-Version як рядок.
# Опційно приймає timestamp як дату та час через параметр запиту (якщо не вказано — автоматично підставляє поточний момент).
# Повертає JSON-відповідь із:
# привітанням користувачу (Hello, user {user_id})
# отриманим timestamp
# отриманою версією клієнта.

from fastapi import FastAPI, Path, Query, Header
from datetime import datetime


app = FastAPI()


@app.get("/users/{user_id}")
async def greet_user(
    user_id: int = Path(..., title="ID користувача", ge=1),
    timestamp: datetime = Query(default=None, title="Час запиту"),
    x_client_version: str = Header(..., title="Версія клієнтського додатку")
):
    if timestamp is None:
        timestamp = datetime.now()
    return {
        "message": f"Hello, user {user_id}",
        "timestamp": timestamp.isoformat(),
        "client_version": x_client_version
    }
