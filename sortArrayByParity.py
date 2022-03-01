def sortArrayByParity(A):
    size = len(A)
    arr = [0] * size
    i = 0
    j = size - 1
    for x in range(0, size):
        if (i > j):
            break
        if (A[x] % 2 == 0):
            arr[i] = A[x]
            i += 1
        else:
            arr[j] = A[x]
            j -= 1
    return arr