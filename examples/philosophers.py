from asyncio import wait, sleep, Lock, gather, get_event_loop
from random import lognormvariate


async def philosopher(name, left_fork, right_fork, dinner):
    eaten = 0
    while dinner.served:
        print('%s waiting for forks' % name)
        done, missed = await wait(
            (
                dinner.get_fork(left_fork),
                dinner.get_fork(right_fork)
            ),
            timeout=dinner.timeout()
        )
        # The philosopher got both forks, simulate eating
        if not missed:
            eaten += 1
            print('%s eating ... %d' % (name, eaten))
            await sleep(dinner.timeout())
            print('%s finished eating' % name)
            # Eaten all the courses, stop dinner
            if eaten >= dinner.courses:
                dinner.served = False
                break
        else:
            # cancel the missed tasks.
            # Important otherwise the lock will be acquired when
            # we don't want to
            for task in missed:
                task.cancel()

        for task in done:
            task.result().release()

    return name, eaten


class Dinner:
    """Dinner organiser
    """
    def __init__(self, mu=0.3, sigma=0.4, courses=10):
        self.served = True
        self.courses = courses
        self.mu = mu
        self.sigma = sigma

    def timeout(self):
        return lognormvariate(self.mu, self.sigma)

    def serve(self, N=5):
        philosophers = []
        first = right = Lock()
        # Create philosophers (coroutines)
        for n in range(1, N+1):
            left = right
            right = Lock() if n < N else first
            p = philosopher('philosopher-%d' % n, left, right, self)
            philosophers.append(p)
        #
        # Run the app
        result = get_event_loop().run_until_complete(gather(*philosophers))
        #
        # print the results
        for name, eaten in sorted(result, key=lambda v: v[1]):
            print('%s %s' % (name, 'o'*eaten))

    async def get_fork(self, lock):
        await lock.acquire()
        return lock


if __name__ == '__main__':
    dinner = Dinner()
    dinner.serve()
