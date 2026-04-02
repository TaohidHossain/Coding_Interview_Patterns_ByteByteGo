from typing import List

def pair_sum_ordered_brute_force(nums: List[int], target: int) -> List[int]:
    """
    Time Complexiy: O(n^2)
    Space Complexity: O(1)
    """
    n = len(nums)
    
    for i in range(n):
        for j in range(i+1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    
    return []


print(pair_sum_ordered_brute_force([-5, -3, 1, 3, 4, 5], 7))
print(pair_sum_ordered_brute_force([-5, -3, 1, 3, 4, 5], 31))


def pair_sum_two_pointer(nums: List[int], target: int) -> List[int]:
    """
    Time Complexiy: O(n)
    Space Complexity: O(1)
    """
    left, right = 0, len(nums) - 1

    while left < right:
        sum = nums[left] + nums[right]
        if sum < target:
            left += 1
        elif sum > target:
            right -= 1
        else:
            return [left, right]
    
    return []

print(pair_sum_two_pointer([-5, -3, 1, 3, 4, 5], 7))
print(pair_sum_two_pointer([-5, -3, 1, 3, 4, 5], 16))
print(pair_sum_two_pointer([], 16))