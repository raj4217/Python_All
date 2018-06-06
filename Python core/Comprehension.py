dict = {n: n * 2 for n in range(5)}
print(dict)


num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lst = []

for n in num:
    lst.append(n * n)
lst = list(map(lambda n: n * n, num))
lst = [n**2 for n in num]

for n in num:
    lst.append(n * n)
lst = list(filter(lambda n: n % 2 == 0, num))
lst = [n for n in num if n % 2 == 0]

for a in 'abcd':
    for b in range(4):
        lst.append((a, b))
lst = [(a, b) for a in 'abcd' for b in range(4)]

# print(lst)


# import timeit
# # num = [1,2,3,4,5,6,7,8,9,10]
# def normal():
#     num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     # lst = num.copy()
#     lst = []
#     for n in num: lst.append(n ** 2)
#     print(lst)
#
#
# def fast():
#     num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     lst = [n**2  for n in num]
#     print(lst)
#
# timeit.timeit(normal(),number=10000)
# timeit.timeit(fast(),number=10000)
