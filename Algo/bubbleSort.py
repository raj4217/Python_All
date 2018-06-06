def bubsort(arr):
    for j in range(len(arr)):
        swap = False
        for i in range(len(arr) - j - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i] = arr[i + 1], arr[i]
                swap = True
        if swap == False:
            break
    return arr


# arr = list(range(2,10))
# arr = [5, 6, 7, 8, 9, 2, 3, 4]

print(bubsort(arr))
