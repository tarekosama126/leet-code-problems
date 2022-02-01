def twoSum(nums, target):
    arr = []
    x = False
    size = len(nums)
    for i in range(0, size):
        for j in range(i + 1, size):
            if (nums[i] + nums[j] == target):
                arr[0] = i
                arr[1] = j
                x = True
                break

        if (x):
            break
    return arr