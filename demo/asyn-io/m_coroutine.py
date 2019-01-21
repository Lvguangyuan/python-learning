

def consumer():
    r = ''
    while True:
        n = yield r
        print('[Consumer] Consuming %s...' % n)
        r = '200 OK'


def produce(c):
    n = 0
    c.send(None)
    while n < 5:
        n = n + 1
        print('[Producer] Producing %s...' % n)
        r = c.send(n)
        print('[Producer] Consumer return %s' % r)
    c.close()


consumer = consumer()
produce(consumer)