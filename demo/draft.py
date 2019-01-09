

from datetime import datetime


def to_timestamp(time):
    t = datetime.strptime(time, '%Y-%m-%d %H:%M:%S')
    print(t.timestamp())