def calculate_sum(n):
    return sum(range(1, n + 1))

result = calculate_sum(1_000_000)
print(f"Сума = {result}")
      

import asyncio

async def calculate_sum(n):
    return sum(range(1, n + 1))

async def main():
    result = await calculate_sum(1_000_000)
    print(f"Сума = {result}")

asyncio.run(main())