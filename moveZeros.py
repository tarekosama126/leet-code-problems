def moveZeroes(nums):
    i = 0
    j = 1
    size = len(nums) - 1
    while i <= size and j <= size:
        if nums[i] != 0:
            i += 1
            j += 1
        elif nums[i] == 0 and nums[j] != 0:
            temp = nums[j]
            nums[j] = nums[i]
            nums[i] = temp
            i += 1
            j += 1
        elif nums[i] != 0 and nums[j] != 0:
            i += 2
            j += 2
        elif nums[i] == 0 and nums[j] == 0:
            j += 1
    return nums