from fastapi import FastAPI, Header


app = FastAPI()


@app.get("/user-agent/")
async def read_user_agent(user_agent: str = Header(None)):
    if user_agent:
        return {"User-Agent": user_agent}
    else:
        return {"message": "User-Agent header is missing"}
