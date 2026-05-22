from fastapi import FastAPI
import asyncio
import httpx

app = FastAPI()

@app.get("/async-endpoint")
async def read_items():
    await asyncio.sleep(1)  # Імітація повільної операції
    return {"message": "Асинхронна відповідь після 1 секунди очікування"}


@app.get("/btc-price")
async def get_btc_price():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd")
        data = response.json()
        return {"btc_price_usd": data['bitcoin']['usd']}