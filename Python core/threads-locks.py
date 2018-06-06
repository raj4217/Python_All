import threading
import time
lock = threading.Lock()
x = 0
count = 100000


def add2():
    global x
    with lock:
        for _ in range(count):
            x += 2


def add3():
    global x
    with lock:
        for _ in range(count):
            x += 3


def sub4():
    global x
    with lock:
        for _ in range(count):
            x -= 4


def sub1():
    global x
    with lock:
        for _ in range(count):
            x -= 1


t1 = threading.Thread(target=add2)
t2 = threading.Thread(target=sub4)
t3 = threading.Thread(target=add3)
t4 = threading.Thread(target=sub1)

t1.start()
t2.start()
t3.start()
t4.start()

t1.join()
t2.join()
t3.join()
t4.join()

print(x)
