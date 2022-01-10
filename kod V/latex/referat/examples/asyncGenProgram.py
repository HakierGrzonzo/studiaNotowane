import asyncio


async def main():
    data = await getOneDataAsync()
    while True:
        if data is None:
            # No data left
            break
        data = processData(data)
        # Get user input for previous data and fetch next data
        (new_data, user_decision,) = await asyncio.gather(
            getOneDataAsync(),
            askUserForActionAsync(data),
        )
        if user_decision:
            saveData(data)

        data = new_data

asyncio.run(main())
