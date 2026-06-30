from fastapi import FastAPI, Header, HTTPException
import uvicorn


app = FastAPI()


@app.get("/items/")
async def read_items(
    user_agent: str = Header(None),
    x_token: str = Header(...)
):
    if x_token != "secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


    return {"User-Agent": user_agent, "X-Token": x_token}

if __name__ == "__main__":
    uvicorn.run(app)


# from fastapi.responses import JSONResponse, HTMLResponse


# @app.get("/info/")
# async def get_info(accept: str = Header(default="application/json")):
#     data = {"message": "This is a JSON response"}


#     if "application/json" in accept:
#         return JSONResponse(content=data)


#     elif "text/html" in accept:
#         html_content = "<html><body><h1>This is an HTML response</h1></body></html>"
#         return HTMLResponse(content=html_content)


#     else:
#         raise HTTPException(status_code=406, detail="Not Acceptable")