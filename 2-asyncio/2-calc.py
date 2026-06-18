import time
import asyncio
import random


def calculate_sum_sync(n):
    return sum(range(1, n + 1))


async def calculate_sum_async(n):
    return sum(range(1, n + 1))


N = 20_000_000
RUNS = 45

sync_times = []
async_times = []


async def run_async():
    start = time.perf_counter()
    await calculate_sum_async(N)
    return time.perf_counter() - start


for _ in range(RUNS):
    if random.choice([True, False]):
        # Спочатку sync
        start = time.perf_counter()
        calculate_sum_sync(N)
        sync_times.append(time.perf_counter() - start)

        async_times.append(asyncio.run(run_async()))
    else:
        # Спочатку async
        async_times.append(asyncio.run(run_async()))

        start = time.perf_counter()
        calculate_sum_sync(N)
        sync_times.append(time.perf_counter() - start)


print(f"Синхронно:  {sum(sync_times) / len(sync_times):.6f} сек")
print(f"Асинхронно: {sum(async_times) / len(async_times):.6f} сек")