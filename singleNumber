def singleNumber(nums) -> int:
    nums.sort()
    i = 0
    while i != len(nums):
        if i + 1 >= len(nums):
            return nums[i]
        if nums[i] == nums[i + 1]:
            i = i + 2
            continue
        else:
            return nums[i]