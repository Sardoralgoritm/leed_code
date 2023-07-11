class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = bin(n)
        return ans[2:].count("1")
