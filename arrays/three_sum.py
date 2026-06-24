from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Solves the 3Sum problem: Find all unique triplets in the array which gives the sum of zero.
        Uses a sorting + two-pointer approach.
        Complexity: O(N^2) time, O(1) extra space (excluding output).
        """
        nums.sort()
        result = []
        n = len(nums)
        
        for i in range(n - 2):
            # Skip duplicate elements for the first position
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            # Use two pointers to find the remaining two elements
            left, right = i + 1, n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    # Skip duplicates for the second and third positions
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        
        return result