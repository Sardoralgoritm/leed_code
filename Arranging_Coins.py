class Solution:
    def arrangeCoins(self, n: int) -> int:
        def mysum(n: int) -> int:
            return n * (n + 1) // 2

        i = 1
        while True:
            if mysum(i) == n:
                return i
            elif mysum(i) > n:
                return i - 1
            i += 1
