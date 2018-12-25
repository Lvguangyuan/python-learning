from multiprocessing import Process, Queue
import os, time, random


def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s in queue....' % value)
        q.put(value)
        time.sleep(random.random())


def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s in queue...' % value)


if __name__ == '__main__':
    # 父进程创建Queue, 并传给各个子进程
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pr.start()
    # 等待pw结束
    pw.join()
    # 强制结束pr
    pr.terminate()