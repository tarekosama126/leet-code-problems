def findNumbers(nums):
    count = 0
    for i in range(0, len(nums)):
        num = str(nums[i])
        if (len(num) % 2 == 0):
            count += 1
    return count
