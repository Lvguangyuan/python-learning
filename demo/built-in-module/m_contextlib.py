
# 1.
class Query(object):

    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print('Enter.')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print('Error.')
        else:
            print('End.')

    def query(self):
        print('Query info about %s ' % self.name)

# 2.
from contextlib import contextmanager


class Query2(object):

    def __init__(self, name):
        self.name = name

    def query(self):
        print('Query2 of %s' % self.name)


@contextmanager
def create_query2(name):
    print('Query2 Begin')
    q = Query2(name)
    yield q
    print('Query2 End')


# 3.
@contextmanager
def tag(name):
    print('<%s>' % name)
    yield
    print('</%s>' % name)


# 4.
from contextlib import closing
from urllib.request import urlopen


with closing(urlopen('https://www.python.org')) as page:
    for line in page:
        print(line)


@contextmanager
def closing(thing):
    try:
        yield thing
    finally:
        thing.close()