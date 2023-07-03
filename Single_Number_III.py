class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        nums.sort()
        ls = []
        if len(nums) == 1:
            return nums[0]
        for i in range(len(nums)):
            if i > 0 and i+1 < len(nums):
                if nums[i] != nums[i-1] and nums[i] != nums[i+1]:
                    ls.append(nums[i])
            elif i == 0:
                if nums[i] != nums[i+1]:
                    ls.append(nums[i])
            else:
                if nums[i] != nums[i-1]:
                    ls.append(nums[i])
        return ls
