from fastapi import FastAPI, Query
import uvicorn
from typing import Optional


app = FastAPI()


items = []



@app.get("/")
def index():
    return {"status": "active"}


@app.get("/items/")
async def read_items(
    skip: int = Query(0, description="Кількість записів для пропуску"),
    limit: int = Query(10, description="Максимальна кількість записів")
):
    # items = get_items_from_db(skip, limit)
    return {"items": items}






@app.get("/search/")
async def search_items(q: str = Query(..., description="Пошуковий запит")):
    return {"query": q}




@app.get("/filter/")
async def filter_items(category: Optional[str] = Query(None)):
    return {"category": category}


if __name__ == "__main__":
    uvicorn.run(app)
