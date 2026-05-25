from fastapi import FastAPI, Header, HTTPException


app = FastAPI()


@app.get("/data/")
async def get_data(
    authorization: str = Header(...),
    x_custom_header: str = Header(None)
):
    if authorization != "Bearer mysecrettoken":
        raise HTTPException(status_code=401, detail="Unauthorized")


    return {
        "message": "Success",
        "X-Custom-Header": x_custom_header
    }