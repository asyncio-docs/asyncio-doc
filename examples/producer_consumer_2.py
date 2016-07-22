import asyncio
import random


async def produce(queue, n):
    for x in range(n):
        print('producing {}...'.format(x))
        await asyncio.sleep(random.random())
        await queue.put(x)


async def consume(queue):
    while True:
        x = await queue.get()
        print('consuming {}...'.format(x))
        await asyncio.sleep(random.random())
        queue.task_done()


async def run(n):
    queue = asyncio.Queue()
    consumer = asyncio.ensure_future(consume(queue))
    await produce(queue, n)
    await queue.join()
    consumer.cancel()


loop = asyncio.get_event_loop()
loop.run_until_complete(run(10))
loop.close()
