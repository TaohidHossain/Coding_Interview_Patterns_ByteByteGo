from typing import List

def shift_zeros_to_the_end(nums: List[int]) -> None:
    left = 0

    for right in range(len(nums)):
        if nums[right] != 0 and right != left:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1

arr = [0, 1, 0, 3, 1]
shift_zeros_to_the_end(arr)
print(arr)

arr = []
shift_zeros_to_the_end(arr)
print(arr)

arr = [0]
shift_zeros_to_the_end(arr)
print(arr)

arr = [1]
shift_zeros_to_the_end(arr)
print(arr)

arr = [0, 0, 0]
shift_zeros_to_the_end(arr)
print(arr)

arr = [1, 3, 4]
shift_zeros_to_the_end(arr)
print(arr)

arr = [1, 2, 3, 0, 0]
shift_zeros_to_the_end(arr)
print(arr)

arr = [0, 0, 0, 3, 1]
shift_zeros_to_the_end(arr)
print(arr)