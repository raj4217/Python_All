def binarySearch(arr, num, hi, lo):
    if hi < lo:
        return -1

    mid = (hi + lo) // 2

    if num == arr[mid]:
        return mid

    if arr[lo] < arr[mid]:
        if arr[lo] <= num <= arr[mid]:
            return binarySearch(arr, num, mid - 1, lo)
        return binarySearch(arr, num, hi, mid + 1)

    if arr[mid] <= num <= arr[hi]:
        return binarySearch(arr, num, hi, mid + 1)
    return binarySearch(arr, num, mid - 1, lo)


# def binarySearch(arr, num, hi, lo):

#     def func(arr, num, hi, lo):
#         while hi > 0:
#             mid = (hi + lo) // 2
#             print(mid, hi, lo)
#             if num == arr[mid]:
#                 return mid
#             elif num > arr[mid]:
#                 return func(arr, num, hi, mid + 1)
#             else:
#                 return func(arr, num, mid - 1, lo)
#         return -1

#     for a in range(hi - 1):
#         if arr[a] > arr[a + 1]:
#             mid = a + 1
#     print(mid, hi, lo)
#     if num == arr[mid]:
#         return mid
#     elif arr[hi - 1] >= num > arr[mid]:
#         lo = mid + 1

#     else:
#         hi = mid - 1
#     print(mid, hi, lo)

#     return func(arr, num, hi, lo)


# arr = [5, 6, 7, 8, 9, 2, 3, 4]
arr = list(range(2,10))
num = 6
res = binarySearch(arr, num, len(arr), 0)
if res != -1:
    print(f'Num found at position {res}')
else:
    print('Num not found!')
