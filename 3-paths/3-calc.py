from fastapi import FastAPI, HTTPException
import math

from pydantic import BaseModel


app = FastAPI()


class ExpressionRequest(BaseModel):
    expression: str


@app.post("/calc")
def calc(data: ExpressionRequest):
    expression = data.expression

    actions = ["+", "-", "*", "/"]

    n1 = ""
    n2 = ""
    action = None

    for e in expression + "n":
        if action and (e in actions or e == "n"):
            n1 = float(n1)
            n2 = float(n2)

            results = {"+": n1 + n2, "-": n1 - n2, "*": n1 * n2, "/": n1 / n2}

            n1 = str(results[action])
            n2 = ""
            action = e if e != "n" else None

            continue

        if action is None:
            if e not in actions:
                n1 += e
            else:
                action = e

        else:
            n2 += e

    return {"result": float(n1)}


@app.post("/priority_calc")
def priority_calc(data: ExpressionRequest):

    # Функція виконує одну математичну операцію
    def apply_operation(numbers, operator):

        # Беремо два останніх числа зі стеку
        b = numbers.pop()
        a = numbers.pop()

        # Словник доступних операцій
        operations = {
            "+": a + b,
            "-": a - b,
            "*": a * b,
            "/": a / b
        }

        # Додаємо результат назад у стек
        numbers.append(operations[operator])

    # Функція повертає пріоритет операції
    def priority(operator):

        priorities = {
            "+": 1,
            "-": 1,
            "*": 2,
            "/": 2
        }

        return priorities[operator]

    # Отримуємо вираз із body запиту
    expression = data.expression

    # Стек чисел
    numbers = []

    # Стек операторів
    operators = []

    # Поточне число, яке збираємо посимвольно
    current_number = ""

    # Додаємо пробіл у кінець,
    # щоб обробити останнє число
    for char in expression + " ":

        # Якщо символ — цифра або крапка,
        # додаємо його до поточного числа
        if char.isdigit() or char == ".":
            current_number += char

        # Якщо символ — оператор
        elif char in "+-*/":

            # Якщо число зібране — додаємо у стек
            if current_number:
                numbers.append(float(current_number))
                current_number = ""

            # Поки у стеку є оператори
            # з більшим або рівним пріоритетом —
            # виконуємо їх
            while (
                operators
                and priority(operators[-1]) >= priority(char)
            ):
                apply_operation(numbers, operators.pop())

            # Додаємо поточний оператор у стек
            operators.append(char)

    # Додаємо останнє число у стек
    if current_number:
        numbers.append(float(current_number))

    # Виконуємо залишкові операції
    while operators:
        apply_operation(numbers, operators.pop())

    # Повертаємо фінальний результат
    return numbers[0]


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app)
