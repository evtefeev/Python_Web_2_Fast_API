import asyncio
import time


async def simple_delay():
    print("Початок задачі")
    await asyncio.sleep(2)
    # time.sleep(2)
    print("Завершення задачі")


tasks = [simple_delay(), simple_delay(), simple_delay(), simple_delay()]


async def main():
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
