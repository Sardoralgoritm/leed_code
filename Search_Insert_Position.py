class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        for i, a in enumerate(nums):
            if a > target:
                return i
        return len(nums)
