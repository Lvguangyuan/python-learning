import threading


local_name = threading.local()


def process_student():
    name = local_name.name
    print('Hello, %s in %s' % (name, threading.current_thread().name))


def process_thread(name):
    local_name.name = name
    process_student()


t1 = threading.Thread(target=process_thread, args=('Blue',), name='Thread-1')
t2 = threading.Thread(target=process_thread, args=('Lily',), name='Thread-2')
t1.start()
t2.start()
t1.join()
t2.join()
