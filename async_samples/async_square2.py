import asyncio


async def square(number: int) -> int:
    # some code
    # write in db
    return number * number


async def main() -> None:
    x = await square(10)
    print(f'x={x}')

    y = await square(5)
    print(f'y={y}')

    print(f'total={x+y}')

if __name__ == '__main__':
    asyncio.run(main())