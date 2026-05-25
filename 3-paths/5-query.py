from fastapi import FastAPI, Query


app = FastAPI()


@app.get("/items/")
async def read_items(
    skip: int = Query(0, title="Кількість записів для пропуску"),
    limit: int = Query(10, title="Максимальна кількість записів")
):
    items = get_items_from_db(skip, limit)
    return {"items": items}



from typing import Optional


@app.get("/search/")
async def search_items(q: str = Query(..., description="Пошуковий запит")):
    return {"query": q}




@app.get("/filter/")
async def filter_items(category: Optional[str] = Query(None)):
    return {"category": category}
