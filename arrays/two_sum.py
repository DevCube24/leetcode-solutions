"""
Two Sum - LeetCode Easy

Problem:
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Approach:
Use a hash map (dictionary) to store the value and its index. For each number, check if (target - num) exists in the map.
Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    prevMap = {}  # val : index

    for i, n in enumerate(nums):
        diff = target - n
        if diff in prevMap:
            return [prevMap[diff], i]
        prevMap[n] = i

# Test cases
if __name__ == "__main__":
    print(twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]
    print(twoSum([3, 2, 4], 6))       # Output: [1, 2]
