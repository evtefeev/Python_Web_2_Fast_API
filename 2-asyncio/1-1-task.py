import asyncio
import time


async def make_pizza():
    print("🍕 Починаю готувати піцу...")
    await asyncio.sleep(3)  # чекаємо, але не блокуємо програму
    print("🍕 Піца готова!")


async def make_tea():
    print("☕ Починаю робити чай...")
    await asyncio.sleep(2)
    print("☕ Чай готовий!")


async def main():
    tasks = [make_pizza(), make_tea()]
    await asyncio.gather(*tasks)


asyncio.run(main())