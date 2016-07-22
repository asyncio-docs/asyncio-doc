import asyncio
import random


async def produce(n):
    for item in range(n):
        print('producing {}...'.format(item))
        await asyncio.sleep(random.random())
        await queue.put(item)
    # Indicate the producer is done
    await queue.put(None)


async def consume():
    while True:
        item = await queue.get()
        if item is None:
            break
        print('consuming {}...'.format(item))
        await asyncio.sleep(random.random())


queue = asyncio.Queue()
asyncio.ensure_future(produce(10))

loop = asyncio.get_event_loop()
loop.run_until_complete(consume())
loop.close()
