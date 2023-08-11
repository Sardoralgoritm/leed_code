def kabisa(n: int) -> bool:
    return True if n % 400 == 0 or (n % 100 != 0 and n % 4 == 0) else False

class Solution:
    def dayOfYear(self, a: str) -> int:
        ans = 0
        b = int(a.split("-")[1])
        for i in range(1,b):
            if i == 2:
                if kabisa(int(a.split("-")[0])):
                    ans += 29
                else:
                    ans += 28
            elif i < 8:
                if i % 2:
                    ans += 31
                elif i % 2 == 0 and i != 2:
                    ans += 30

            else:
                if i % 2 == 0:
                    ans += 31
                else:
                    ans += 30
        ans += int(a.split("-")[2])
        return ans
