from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/greet/")
def read_greeting(name: str = Query(None, description="Введіть ваше ім'я")):
    return {"message": "Вітаємо!"}



# from fastapi import FastAPI
# app = FastAPI()

# @app.get("/greet/{name}")
# def read_greeting(name: str):
#     return {"message": f"Вітаємо, {name}!"}

# @app.get("/greet/")
# def greet(name: str = Query(None, description="Введіть ваше ім'я")):

#     if name:
#         return {"message": f"Вітаємо, {name}!"}
#     else:
#         return {"message": "Вітаємо, Гість!"}

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)