#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# task_master.py


import queue
from multiprocessing.managers import BaseManager
import random

# 发送任务的队列
task_queue = queue.Queue()
# 接收结果的队列
result_queue = queue.Queue()


def return_task_queue():
    global task_queue
    return task_queue


def return_result_queue():
    global result_queue
    return result_queue


class QueueManager(BaseManager):
    pass


if __name__ == '__main__':
    # 把两个Queue都注册到网络上
    QueueManager.register('get_task_queue', callable=return_task_queue)
    QueueManager.register('get_result_queue', callable=return_result_queue)
    # 绑定端口5000，设置验证码'abc'
    manager = QueueManager(address=('', 5000), authkey=b'abc')
    manager.start()
    # 获取通过网络访问的Queue对象
    task = manager.get_task_queue()
    result = manager.get_result_queue()

    for i in range(10):
        n = random.randint(0, 1000)
        print('Put task %d...' % n)
        task.put(n)
    print('Try get results...')

    for i in range(10):
        n = result.get(timeout=10)
        print('Results: %s' % n)

    manager.shutdown()
    print('master exit.')
