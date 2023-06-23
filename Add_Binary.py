class Solution:
    def addBinary(self, a: str, b: str) -> str:
        c = int(a,2)
        b = int(b,2)
        ans = bin(c+b)
        return ans[2::]
