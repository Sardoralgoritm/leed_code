class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ls = list(magazine)
        cnt = 0
        for i in ransomNote:
            if i in ls:
                cnt = 1
                ls.remove(i)
            else:
                cnt = 0
                break
        if cnt:
            return True
        else:
            return False
        
