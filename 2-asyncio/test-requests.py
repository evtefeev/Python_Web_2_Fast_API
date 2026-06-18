# load_test.py

import asyncio
import aiohttp
import time


BASE_URL = "http://127.0.0.1:8000"

TOTAL_REQUESTS = 200
CONCURRENT = 100

sem = asyncio.Semaphore(CONCURRENT)


async def fetch(session, endpoint):
    async with sem:

        start = time.perf_counter()

        async with session.get(f"{BASE_URL}{endpoint}") as resp:
            await resp.text()

        return time.perf_counter() - start


async def test(endpoint):

    async with aiohttp.ClientSession() as session:

        start = time.perf_counter()

        tasks = [
            fetch(session, endpoint)
            for _ in range(TOTAL_REQUESTS)
        ]

        results = await asyncio.gather(*tasks)

        total = time.perf_counter() - start

    print(f"\n{endpoint}")
    print(f"Total time: {total:.2f}")
    print(f"Average: {sum(results)/len(results):.2f}")
    print(f"RPS: {TOTAL_REQUESTS/total:.2f}")


async def main():
    await test("/sync")
    await test("/async")


asyncio.run(main())