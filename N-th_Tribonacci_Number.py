class Solution:
    def tribonacci(self, n: int) -> int:
        ls = []
        ls.append(0)
        ls.append(1)
        ls.append(1)
        for i in range(n-2):
            ls.append(ls[-1] + ls[-2] + ls[-3])
        return ls[-1] if n != 0 else 0
