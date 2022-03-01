from typing import List
def rotate_array(nums: List[int], k: int) -> None:
    output = [0] * len(nums)
    for i in range(0, len(nums)):
        output[(i + k) % len(nums)] = nums[i]
    print(output)