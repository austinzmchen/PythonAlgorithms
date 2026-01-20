def chunk(arr, size):
    res = []
    curr = []

    for i, n in enumerate(arr):
        curr.append(n)

        if (i + 1) % size == 0:
            res.append(list(curr))
            curr = []

    if curr:
        res.append(curr)
    
    return res


print(chunk(arr = [1,2,3,4,5], size = 1))
print(chunk(arr = [1,9,6,3,2], size = 3))