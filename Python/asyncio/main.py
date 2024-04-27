import asyncio

async def getData(delay, id):
	print(f"Getting data... for id:{id}")
	await asyncio.sleep(delay)
	print("Data fetched!")
	return {"data" : id}

async def main():
	print("Start of main coroutine")

	results = await asyncio.gather(getData(1, 1),getData(3, 2))

	for result in results:
		print(f"Received data: {result}")

	print("End of main coroutine")


asyncio.run(main())