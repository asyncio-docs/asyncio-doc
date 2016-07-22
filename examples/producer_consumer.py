import asyncio
import random


async def produce(n):
    for x in range(n):
        print('producing {}...'.format(x))
        await asyncio.sleep(random.random())
        await queue.put(x)


async def consume():
    while True:
        x = await queue.get()
        print('consuming {}...'.format(x))
        await asyncio.sleep(random.random())
        queue.task_done()


queue = asyncio.Queue()
producer = asyncio.ensure_future(produce(10))
consumer = asyncio.ensure_future(consume())
waiter = asyncio.gather(producer, queue.join())

loop = asyncio.get_event_loop()
loop.run_until_complete(waiter)
