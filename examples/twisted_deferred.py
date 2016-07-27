from twisted.internet import defer
from twisted.internet import reactor


def multiply(x):
    result = x * 2
    d = defer.Deferred()
    reactor.callLater(1.0, d.callback,
                      result)
    return d


def step1(x):
    return multiply(x)


def step2(result):
    print("result: %s" % result)

    reactor.stop()


d = defer.Deferred()
d.addCallback(step1)
d.addCallback(step2)
d.callback(5)

reactor.run()

