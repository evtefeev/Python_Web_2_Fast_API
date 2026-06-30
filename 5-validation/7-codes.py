from fastapi import FastAPI, status


app = FastAPI()
names = []

@app.post("/items/", status_code=status.HTTP_201_CREATED)
async def create_item(name: str):
    names.append(name)
    return {"name": name}


@app.get("/items/{name}")
async def read_item(name: str):
    if name not in names:
        return {"error": "No item found"}, status.HTTP_404_NOT_FOUND
    return {"name": name}


@app.get("/items/")
async def read_items():
    if names == []:
        return [], status.HTTP_204_NO_CONTENT
    else:
        return names, status.HTTP_200_OK


@app.put("/items/{item_id}")
async def update_item(item_id: int):
    return {"item_id": item_id, "message": "Item updated"}, status.HTTP_200_OK


@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    return {"message": "Item deleted"}, status.HTTP_202_ACCEPTED