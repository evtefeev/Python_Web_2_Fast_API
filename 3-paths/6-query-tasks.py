from fastapi import FastAPI, Query
import uvicorn
from typing import Optional


app = FastAPI()


items = []
users = []


@app.get("/items/search/")
async def search_items(q: Optional[str] = Query(None, max_length=50)):
    items = [{"item_id": "Foo"}, {"item_id": "Bar"}]
    if q:
        items = [item for item in items if q.lower() in item["item_id"].lower()]
    return {"items": items}


@app.get("/users/")
async def get_users(
    skip: int = Query(0, ge=0, description="Кількість записів для пропуску"),
    limit: int = Query(10, gt=0, le=100, description="Максимум записів у відповіді"),
):
    # users = get_users_from_db(skip, limit)
    return {"users": users}


if __name__ == "__main__":
    uvicorn.run(app)
