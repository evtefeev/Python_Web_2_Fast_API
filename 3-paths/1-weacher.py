from fastapi import FastAPI, HTTPException


app = FastAPI()


weather_data = {
    "Київ": "Ясно, +20°C",
    "Львів": "Хмарно, +18°C",
    "Одеса": "Дощ, +22°C"
}


@app.get("/weather/{cit}")
def get_weather(city: str):
    weather = weather_data.get(city)
    if weather:
        return {"city": city, "weather": weather}
    raise HTTPException(status_code=404, detail="Місто не знайдено")