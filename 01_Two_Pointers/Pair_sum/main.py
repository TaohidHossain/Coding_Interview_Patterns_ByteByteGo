from typing import List


def pair_sum_brutte_force(nums: List[int], target: int) -> List[int]:
    """
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    for i in range(len(nums)):
        for j in range(1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

    return []

def pair_sum(nums: List[int], target: int) -> List[int]:
    map = {}

    for i, val in enumerate(nums):
        if target - val in map:
            return [map[target - val], i]
        map[val] = i

    return []



print(pair_sum([-1, 3, 4, 2], 3))
print(pair_sum([], 3))
print(pair_sum([1], 3))
print(pair_sum([1, 1, 1], 3))
print(pair_sum([3, -4, 1, 100, 31, -3], 0))