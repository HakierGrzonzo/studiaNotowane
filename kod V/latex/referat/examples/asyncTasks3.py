import asyncio


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def main():
    await say_after(2, "hello ..."),
    await say_after(3, "... world"),

asyncio.run(main())
