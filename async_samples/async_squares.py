import asyncio

async def square(number: int) -> int:
    return number * number


result = asyncio.run(square(10))
print(result)