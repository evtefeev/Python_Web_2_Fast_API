from fastapi import FastAPI
import time

app = FastAPI()

@app.get("/sync")
def sync_endpoint():
    time.sleep(2) 
    return {"message": "Синхронний запит завершений"}

@app.get("/async")
async def async_endpoint():
    await time.sleep(2)
    return {"message": "Асинхронний запит завершений"}