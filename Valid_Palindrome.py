class Solution:
    def isPalindrome(self, s: str) -> bool:
        ls = []
        if s == " " or s ==".":
            return True
        for i in s:
            if i.isalnum():
                ls.append(i)
        ans = "".join(ls)
        ans = ans.lower()
        if ans == ans[::-1]:
            return True
        else:
            return False
