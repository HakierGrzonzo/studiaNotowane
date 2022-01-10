import asyncio
from time import sleep


async def say_after(delay, what):
    sleep(delay)
    print(what)


async def main():
    await asyncio.gather(
        say_after(2, "hello ..."),
        say_after(3, "... world"),
    )

asyncio.run(main())
