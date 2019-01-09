#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# task_worker.py
from multiprocessing.managers import BaseManager
import time
from multiprocessing import Queue


class QueueManager(BaseManager):
    pass


# 该QueueManager只用于获取Queue，仅注册名字即可
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

server_addr = '127.0.0.1'
print('Connect to server %s ...' % server_addr)
m = QueueManager(address=(server_addr, 5000), authkey=b'abc')
m.connect()

task = m.get_task_queue()
result = m.get_result_queue()
for i in range(10):
    try:
        n = task.get(timeout=1)
        print('Run task %d * %d' % (n, n))
        r = '%d * %d = %d' % (n, n, n * n)
        time.sleep(1)
        result.put(r)
    except Queue.empty:
        print('task queue is empty.')
print('worker exit.')
