from typing import List

def largest_container(heights: List[int]) -> int:
    """
    Time Complexity : O(n)
    Space Complexity: O(1)
    """
    max_water = 0
    left, right = 0, len(heights) - 1

    while(left < right):
        water = min(heights[left], heights[right]) * (right - left)
        max_water = max(max_water, water)

        if left < right:
            left += 1
        elif right > left:
            right -= 1
        else:
            left += 1
            right -= 1

    return max_water


print(largest_container([]))
print(largest_container([1]))
print(largest_container([0, 1, 0]))
print(largest_container([6, 6, 6, 6, 6]))
print(largest_container([1, 2, 3]))
print(largest_container([3, 2, 1]))