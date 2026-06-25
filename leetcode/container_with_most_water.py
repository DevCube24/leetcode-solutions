from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Find two lines that together with the x-axis form a container, 
        such that the container contains the most water.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        l, r = 0, len(height) - 1
        max_area = 0
        
        while l < r:
            # Calculate current area
            current_height = min(height[l], height[r])
            current_width = r - l
            max_area = max(max_area, current_height * current_width)
            
            # Move the pointer pointing to the shorter line
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
                
        return max_area
