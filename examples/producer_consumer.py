import asyncio
import random


async def produce(queue, n):
    for x in range(1, n + 1):
        # produce an item
        print('producing {}/{}'.format(x, n))
        # simulate i/o operation using sleep
        await asyncio.sleep(random.random())
        item = str(x)
        # put the item in the queue
        await queue.put(item)

    # indicate the producer is done
    await queue.put(None)


async def consume(queue):
    while True:
        # wait for an item from the producer
        item = await queue.get()
        if item is None:
            # the producer emits None to indicate that it is done
            break

        # process the item
        print('consuming item {}...'.format(item))
        # simulate i/o operation using sleep
        await asyncio.sleep(random.random())


loop = asyncio.get_event_loop()
queue = asyncio.Queue(loop=loop)
asyncio.ensure_future(produce(queue, 10), loop=loop)
loop.run_until_complete(consume(queue))
loop.close()
