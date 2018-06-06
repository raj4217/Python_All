def insertSrt(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            arr[j + 1] = key
    return arr

# def insertSrt(arr):
#     for i in range(1, len(arr)):
#         swap = False
#         for j in range(i - 1):
#             if arr[j] > arr[i]:
#                 arr.insert(j, arr[i])
#                 del arr[i]
#                 swap = True
#             if swap == True:
#                 break
#     return arr


arr = [5, 6, 7, 8, 9, 2, 3, 4]
print(insertSrt(arr))
