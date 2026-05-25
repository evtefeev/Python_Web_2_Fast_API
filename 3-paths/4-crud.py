from fastapi import FastAPI


app = FastAPI()


@app.get("/items/")
def read_items():
    return {"message": "List of items"}


@app.post("/items/")
def create_item(item: str):
    return {"message": f"Item '{item}' created"}


@app.put("/items/{item_id}")
def update_item(item_id: int, new_name: str):
    return {"message": f"Item {item_id} updated to '{new_name}'"}


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return {"message": f"Item {item_id} deleted"}

