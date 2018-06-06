def partition(arr, lo, m, hi):
    n1 = m - lo + 1
    n2 = hi - m
    l = [0] * n1
    r = [0] * n2

    lar = arr[lo:n1]
    rar = arr[m + 1:n2]
    for i in range(0, n1):
        l[i] = arr[lo + i]

    for j in range(0, n2):
        r[j] = arr[m + 1 + j]

    print(arr[lo:n1], l, rar, r)

    i, j, k = 0, 0, lo
    # print(n1, n2, i, j, k)
    while i < n1 and j < n2:
        # print(l[i], r[j])
        if l[i] <= r[j]:
            arr[k] = l[i]
            i += 1
        else:
            arr[k] = r[j]
            j += 1
        k += 1
    while i < n1:
        arr[k] = l[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = r[j]
        j += 1
        k += 1


def merge(arr, lo, hi):
    if hi > lo:
        m = (lo + (hi - 1)) // 2

        merge(arr, lo, m)
        merge(arr, m + 1, hi)
        partition(arr, lo, m, hi)


arr = [12, 11, 13, 5, 6, 7]
merge(arr, 0, len(arr) - 1)
print(arr)
