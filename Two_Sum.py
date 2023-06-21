class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ls = []
        cnt = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    ls.append(i)
                    ls.append(j)
                    cnt = 1
                    break
            if cnt:
                break
        return ls
