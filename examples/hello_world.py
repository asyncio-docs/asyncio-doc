import asyncio

async def say(what, when):
    await asyncio.sleep(when)
    print(what)

loop = asyncio.get_event_loop()
loop.create_task(say('hello', 0.5))
loop.create_task(say('world', 1.0))
loop.run_forever()
