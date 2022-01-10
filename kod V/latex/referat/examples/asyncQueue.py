import asyncio

async def getData():
    while True:
        data = await getOneDataAsync()
        if data is None:
            # No data left to read
            break
        yield data

async def insertDataIntoQueue(queue):
    async for data in getData():
        processed_data = processData(data)
        await queue.put(processed_data)

async def getDataGenerator():
    queue = asyncio.Queue(maxsize=10)
    data_task = asyncio.create_task(insertDataIntoQueue(queue))
    while True:
        if queue.empty() and data_task.done():
            # No more data to process
            break
        yield await queue.get()

async def getUserActions():
    for data in getDataGenerator():
        if await askUserForActionAsync(data):
            yield data
    
async def main():
    async for data in getUserActions():
        saveData(data)

asyncio.run(main())
