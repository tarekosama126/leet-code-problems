def rotate(nums, k) -> None:
    print(len(nums))
    loop = 0
    lastindex = len(nums) - 1
    while loop != k:
        temp = nums[lastindex]
        j = lastindex - 1
        for i in range(lastindex, 0, -1):
            nums[i] = nums[j]
            j -= 1
        nums[0] = temp
        loop += 1
        