import asyncio
import aiohttp

async def fetch_page(url):
    timeout = aiohttp.ClientTimeout(10)
    async with aiohttp.ClientSession(loop=loop, timeout=timeout) as session:
        async with session.get(url) as response:
            assert response.status == 200
            return await response.read()

loop = asyncio.get_event_loop()
content = loop.run_until_complete(
    fetch_page('http://python.org'))
print(content)
loop.close()
