from multiprocessing import Pool
import time


def f(n):
    return(n * n)


if __name__ == '__main__':
    t = time.time()
    arr = list(range(101))
    p = Pool(processes=3)
    res = p.map(f, arr)
    # res = []
    # for n in arr:
    #     time.sleep(0.05)
    #     res.append(f(n))
    print(res)
    print('Completed in ', time.time() - t, 'seconds')


# import time
# import multiprocessing


# def deposit(balance, lock):
#     for _ in range(100):
#         time.sleep(0.01)
#         with lock:
#             balance.value += 1


# def withdraw(balance, lock):
#     for _ in range(100):
#         time.sleep(0.01)
#         lock.acquire()
#         balance.value -= 1
#         lock.release()


# if __name__ == '__main__':
#     balance = multiprocessing.Value('i', 200)
#     lock = multiprocessing.Lock()
#     p1 = multiprocessing.Process(target=deposit, args=(balance, lock))
#     p2 = multiprocessing.Process(target=withdraw, args=(balance, lock))
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()
#     print(balance.value)
