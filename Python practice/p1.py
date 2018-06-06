import time
import threading
import multiprocessing
from multiprocessing import Pool

print(dir(threading))

# def cal_square(num, q):  # res, v):
#     # v.value = 4.5
#     print('calculating squares')
#     for id, n in enumerate(num):
#         # time.sleep(3)
#         # print('square:', n * n)
#         # res[id] = n * n
#         q.put(n * n)


# def cal_cube(num):
#     # print('calculating cubes')
#     # for n in num:
#     time.sleep(2)
#         # print('cube:', n**3)
#     return(num**3)

# if __name__=='__main__':
#     array = [2, 3, 4, 5, 6]
#     p = Pool()
#     res = p.map(cal_cube,array)
#     print(res)


# if __name__ == '__main__':
#     arr = [2, 3, 4, 5, 6]
#     # result = multiprocessing.Array('i', 5)
#     # v = multiprocessing.Value('d', 0.0)
#     q = multiprocessing.Queue()
#     p1 = multiprocessing.Process(target=cal_square, args=(arr, q))  # result, v))
#     # p2 = multiprocessing.Process(target=cal_cube, args=(arr,))
#     p1.start()
#     # p2.start()`
#     p1.join()
#     # p2.join()
#     # print(result[:])
#     # print(v.value)
#     while q.empty() is False:
#         print(q.get())
#     print('Done!')


# arr = [2, 3, 4, 5, 6]
# t = time.time()
# cal_square(arr)
# cal_cube(arr)
# t1 = threading.Thread(target=cal_square, args=(arr,))
# t2 = threading.Thread(target=cal_cube, args=(arr,))

# t1.start()
# t2.start()


# t1.join()
# t2.join()
# print('done in :', time.time() - t)
# print('done totally!')
