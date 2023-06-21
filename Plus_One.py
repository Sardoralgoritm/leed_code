class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ls = list(map(str, digits))
        ans = "".join(ls)
        ls.clear()
        sum = int(ans) + 1
        sum = str(sum)
        for i in sum:
            ls.append(int(i))
        return ls
