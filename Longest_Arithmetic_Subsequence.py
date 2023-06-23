class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp = {}  # dynamic programming table
        maxLen = 0  # maximum length of arithmetic subsequence

        for numIndex in range(len(nums)):
            for prevIndex in range(numIndex):
                diff = nums[numIndex] - nums[prevIndex]
                if (prevIndex, diff) in dp:
                    dp[numIndex, diff] = dp[prevIndex, diff] + 1
                else:
                    dp[numIndex, diff] = 2

                maxLen = max(maxLen, dp[numIndex, diff])

        return maxLen
