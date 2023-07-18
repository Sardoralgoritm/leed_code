class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ls = []
        dc = {"2":"abc",
        "3":"def",
        "4":"ghi",
        "5":"jkl",
        "6":"mno",
        "7":"pqrs",
        "8":"tuv",
        "9":"wxyz"}
        if len(digits) == 1:
            for i in dc[digits]:
                ls.append(i)
        if len(digits) == 2:
            for i in dc[digits[0]]:
                for j in dc[digits[1]]:
                    ls.append(i+j)
        if len(digits) == 3:
            for i in dc[digits[0]]:
                for j in dc[digits[1]]:
                    for k in dc[digits[2]]:
                        ls.append(i+j+k)
        if len(digits) == 4:
            for i in dc[digits[0]]:
                for j in dc[digits[1]]:
                    for k in dc[digits[2]]:
                        for d in dc[digits[3]]:
                            ls.append(i+j+k+d)
        return ls
