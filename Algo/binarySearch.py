def binarySearch(arr, num, hi, lo):
    while hi > 0:
        mid = int((hi + lo) / 2)
        if num == arr[mid]:
            return mid
        elif num > arr[mid]:
            return binarySearch(arr, num, hi, mid + 1)
        else:
            return binarySearch(arr, num, mid - 1, lo)
    return -1


arr = [2, 3, 4, 5, 6, 7, 8, 9]
num = 9
res = binarySearch(arr, num, len(arr), 0)
if res != -1:
    print(f'Num found at position {res}')
else:
    print('Num not found!')
