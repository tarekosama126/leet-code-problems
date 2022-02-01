from typing import List
def findMaxLength(nums: List[int]) -> int:
    dict = {0: -1}
    count = 0
    max_length = 0
    for i in range(0, len(nums)):
        if nums[i] == 1:
            count += 1
        else:
            count -= 1

        if count in dict.keys():
            max_length = max(max_length, i - dict[count])
        else:
            dict[count] = i
    return max_length