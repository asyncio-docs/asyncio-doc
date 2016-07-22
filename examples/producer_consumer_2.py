import asyncio
import random


async def produce(queue, n):
    for x in range(n):
        # produce an item (simulate slow proces using sleep)
        print('producing {}...'.format(item))
        await asyncio.sleep(random.random())
        item = str(x)

        await queue.put(item)


async def consume(queue):
    while True:
        # wait for an item from the producer
        item = await queue.get()

        # process the item
        print('consuming {}...'.format(item))
        await asyncio.sleep(random.random())

        # we are done with the item
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
