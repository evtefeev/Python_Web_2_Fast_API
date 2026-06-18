import time
import asyncio


def do_something():
    time.sleep(2)
    print("Завдання завершено")


def main():
    start = time.time()
    do_something()
    do_something()
    end = time.time()
    print(f"Синхронне виконання завершено за {end - start:.2f} секунд")


async def do_something_async():
    await asyncio.sleep(2)
    print("Асинхронне завдання завершено")


async def async_main():
    start = asyncio.get_running_loop().time()
    tasks = [do_something_async(), do_something_async()]

    await asyncio.gather(*tasks)

    end = asyncio.get_running_loop().time()
    print(f"Асинхронне виконання завершено за {end - start:.2f} секунд")


if __name__ == "__main__":
    main()
    asyncio.run(async_main())
