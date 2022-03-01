def removeDuplicates(nums):
    ans = 1
    index = 1
    test = nums[0]
    for i in range(1, len(nums)):
        if test != nums[i]:
            nums[index] = nums[i]
            ans += 1
            index += 1
        test = nums[i]
    return ans