from typing import List
def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    if len(nums1) < len(nums2):
        nums1, nums2 = nums2, nums1
    cache = {}
    for i in nums1:
        if i in cache:
            cache[i] += 1
        else:
            cache[i] = 1
    answer = []
    for i in nums2:
        if i in cache and cache[i] != 0:
            cache[i] -= 1
            answer.append(i)
    return answer