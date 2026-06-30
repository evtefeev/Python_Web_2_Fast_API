from fastapi import FastAPI
import uvicorn


app = FastAPI()


users = []


@app.get("/")
def index():
    return {"status": "active"}


@app.get("/items/")
def read_items():
    return {"items": users}


@app.post("/items/")
def create_item(item: str):
    users.append(item)
    return {"message": f"Item '{item}' created", "id": users.index(item)}


@app.put("/items/{item_id}")
def update_item(item_id: int, new_name: str):
    users[item_id] = new_name
    return {"message": f"Item {item_id} updated to '{new_name}'"}


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    users.pop(item_id)
    return {"message": f"Item {item_id} deleted"}


if __name__ == "__main__":
    uvicorn.run(app)
