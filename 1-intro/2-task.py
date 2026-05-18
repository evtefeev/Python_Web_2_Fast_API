from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

app = FastAPI()



offices = {
    1: {"name": "Центральний офіс", "address": "вул. Головна, 1", "phone": "123-456-7890"},
    2: {"name": "Філія на Півдні", "address": "вул. Південна, 5", "phone": "987-654-3210"}
}



@app.get("/offices")
def get_offices():
    return offices

@app.get("/offices/{office_id}")
def get_office(office_id: int):
    office = offices.get(office_id)
    if office:
        return office
    else:
        raise HTTPException(status_code=404, detail="Офіс не знайдено")

@app.post("/offices")
def add_office(new_office: Dict[str, str]):
    new_id = max(offices.keys(), default=0) + 1
    offices[new_id] = new_office
    return {"message": "Офіс додано", "office_id": new_id}


@app.put("/offices/{office_id}")
def update_office(office_id: int, update_data: Dict[str, str]):
    if office_id not in offices:
        raise HTTPException(status_code=404, detail="Офіс не знайдено")
    offices[office_id].update(update_data)
    return {"message": "Інформацію про офіс оновлено", "office": offices[office_id]}

@app.delete("/offices/{office_id}")
def delete_office(office_id: int):
    if office_id in offices:
        del offices[office_id]
        return {"message": "Офіс видалено"}
    else:
        raise HTTPException(status_code=404, detail="Офіс не знайдено")
