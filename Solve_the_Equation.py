class Solution:
    def solveEquation(self, equation: str) -> str:
        ans = []
        for i, j in enumerate(equation):
            if j == "x" and equation[i - 1].isdigit() and i != 0:
                ans.append("*")
                ans.append("x")
            else:
                ans.append(j)
        ans1 = "".join(ans)
        b, c = ans1.split("=")[0], ans1.split("=")[1]
        x = 0
        cnt = 0
        for i in range(-200, 200):
            b1 = b.replace("x", str(i))
            c1 = c.replace("x", str(i))
            if int(eval(c1)) == int(eval(b1)):
                cnt += 1
                x = i

        if cnt == 1:
            return f"x={x}"
        elif cnt == 0:
            return "No solution"
        else:
            return "Infinite solutions"
