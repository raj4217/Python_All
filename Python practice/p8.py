arr = [3, 4, 5, 1, 2]
for i in range(len(arr)):
    for j in range(len(arr) - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
print(sum(arr[:4]), sum(arr[1:]))
