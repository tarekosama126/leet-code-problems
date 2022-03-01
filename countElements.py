def countElements(arr):
    arr.sort()
    if len(arr) <= 1:
        return 0
    count = 0
    stack = [arr[0]]
    i = 1
    while i < len(arr):
        lastindex = len(stack) - 1
        if arr[i] > stack[lastindex] and arr[i] - stack[lastindex] == 1:
            count += 1
            x = stack.pop(lastindex)
            if x in stack:
                continue
            else:
                stack.append(arr[i])
                i += 1
        else:
            stack.append(arr[i])
            i += 1

    return count