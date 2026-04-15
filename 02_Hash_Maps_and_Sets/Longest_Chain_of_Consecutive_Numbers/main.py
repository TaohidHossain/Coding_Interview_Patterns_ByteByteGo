from typing import List

def longest_chain_of_consecutive_numbers_brute_force(nums: List[int]) -> int:
    """
    Time Compexity: O(n^3)
    Space Complexity: O(1)
    """
    if not nums:
        return 0
    
    longest_chain = 0
    
    for num in nums:
        current_num = num
        current_chain = 1
        while current_num + 1 in nums:
            current_chain += 1
            current_num += 1
        longest_chain = max(longest_chain, current_chain)

    return longest_chain


print(longest_chain_of_consecutive_numbers_brute_force([1, 6, 2, 5, 8, 7, 10, 3]))

def longest_chain_of_consecutive_numbers(nums: List[int]) -> int:
    if not nums:
        return 0
    longest_chain = 0
    num_set = set(nums)

    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_chain = 1
            while current_num + 1 in num_set:
                current_num += 1
                current_chain += 1
            longest_chain = max(longest_chain, current_chain)
    
    return longest_chain


print(longest_chain_of_consecutive_numbers([1, 6, 2, 5, 8, 7, 10, 3]))
print(longest_chain_of_consecutive_numbers([]))
print(longest_chain_of_consecutive_numbers([9, 8, 7, 6, 5, 4, 3, 2, 1]))
print(longest_chain_of_consecutive_numbers([1, 3, 5, 7, 10, 13]))