import tatort
import asyncio

async def main():
	text = await tatort.getTatort()
	print(text)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())