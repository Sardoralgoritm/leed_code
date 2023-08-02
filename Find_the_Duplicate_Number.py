class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dc = set()
        for i in nums:
            if i in dc:
                return i
            else:
                dc.add(i)
