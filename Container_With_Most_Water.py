class Solution:
    def maxArea(self,height:list) -> int:
        left = 0
        max = 0
        right = len(height) - 1
        while left < right:
            if min(height[right], height[left]) * (right - left) > max:
                max = min(height[right], height[left]) * (right - left)
            if height[right] > height[left]:
                left += 1
            elif height[right] < height[left]:
                 right -= 1
            else:
                 left += 1
                 right -= 1
        return max
        
