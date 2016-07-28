"""Get "web pages.

Waiting until one pages is download before getting the next."
"""

import asyncio
from contextlib import closing
import time

from async_page import get_page


def get_multiple_pages(host, port, waits, show_time=True):
    """Get multiple pages.
    """
    start = time.perf_counter()
    pages = []
    tasks = []
    with closing(asyncio.get_event_loop()) as loop:
        for wait in waits:
            tasks.append(get_page(host, port, wait))
        pages = loop.run_until_complete(asyncio.gather(*tasks))
    duration = time.perf_counter() - start
    sum_waits = sum(waits)
    if show_time:
        msg = 'It took {:4.2f} seconds for a total waiting time of {:4.2f}.'
        print(msg.format(duration, sum_waits))
    return pages

if __name__ == '__main__':

    def main():
        """Test it.
        """
        pages = get_multiple_pages(host='localhost', port='8000',
                                   waits=[1, 5, 3, 2])
        for page in pages:
            print(page)

    main()
