from fastapi import FastAPI, HTTPException, Query

app = FastAPI()

@app.get("/calculate")
def calculate(
    op: str = Query(..., description="Операція: '+', '-', '*', '/', 'square'"),
    a: float = Query(..., description="Перший операнд"),
    b: float = Query(None, description="Другий операнд (не потрібен для 'square')")
):
    if op == "+":
        result = a + b
    elif op == "-":
        result = a - b
    elif op == "*":
        result = a * b
    elif op == "/":
        if b == 0:
            raise HTTPException(status_code=400, detail="На нуль ділити не можна")
        result = a / b
    elif op == "square":
        result = a ** 2
    else:
        raise HTTPException(status_code=400, detail="Невідома операція. Використовуйте '+', '-', '*', '/', 'square'")

    return {
        "operation": op,
        "operand1": a,
        "operand2": b,
        "result": result
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)