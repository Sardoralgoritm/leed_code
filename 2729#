class Solution:
    def isFascinating(self, n: int) -> bool:
        ans = str(n) + str(n*2) + str(n*3)
        ls = set()
        for i in ans:
            ls.add(i)
        if '0' in ls:
            return False
        elif len(ls) == 9 and 9 == len(ans):
            return True
        else:
            return False
