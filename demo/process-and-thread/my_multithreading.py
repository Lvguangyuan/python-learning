import time, threading


def loop():
    print('Thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('Thread %s ended.' % threading.current_thread().name)


print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')
t.start()
for value in ['A', 'B', 'C']:
    time.sleep(1)
    print('Thread %s is running %s' % (threading.current_thread().name, value))
t.join()  # 子线程结束后再执行后面的代码
print('Thread %s ended' % threading.current_thread().name)
