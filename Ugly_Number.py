class Solution:
    def isUgly(self, n: int) -> bool:
        cnt = 1
        if n == 1:
            return True
        elif n == 0:
            return False
        while n != 3 and n != 5 and n != 2:
            if n % 5 == 0:
                n //= 5
                cnt = 1
            elif n % 3 == 0:
                n //= 3
                cnt = 1
            elif n % 2 == 0:
                n //= 2
                cnt = 1
            else:
                cnt = 0
                break
        if cnt and (n == 2 or n == 5 or n == 3):
            return True
        else:
            return False
