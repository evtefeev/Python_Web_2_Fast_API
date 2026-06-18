from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict
import uvicorn

app = FastAPI()

offices = {
    1: {"name": "Центральний офіс", "address": "вул. Головна, 1", "phone": "123-456-7890"},
    2: {"name": "Філія на Півдні", "address": "вул. Південна, 5", "phone": "987-654-3210"}
}

# C - Create
# R - Read
# U - Update
# D - Delete 


# C - Create
@app.post('/offices')
def add_office(new_office: Dict[str, str]):
    new_id = max(offices.keys(), default=0) + 1
    offices[new_id] = new_office
    return {"message": "Офіс додано", "office_id": new_id}


# R - Read
@app.get('/offices')
def get_all_offices():
    return offices

# R - Read
@app.get('/offices/{id}')
def get_office(id: int):
    return offices.get(id)


# U - Update
@app.put("/offices/{office_id}")
def update_office(office_id: int, update_data: Dict[str, str]):
    if office_id not in offices:
        raise HTTPException(status_code=404, detail="Офіс не знайдено")
    offices[office_id].update(update_data)
    return {"message": "Інформацію про офіс оновлено", "office": offices[office_id]}


# D - Delete 
@app.delete('/offices')
def delete_office(id: int):
    del offices[id]
    return {"message": "Офіс видалено", "office_id": id}


if __name__ == "__main__":
    uvicorn.run(app)