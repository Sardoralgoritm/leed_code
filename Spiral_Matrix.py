class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        buy = len(matrix)
        en = len(matrix[0])
        ch, un, te, pa = 0, en-1, 0, buy-1
        answer = []
        while ch <= un and te <= pa:
            for i in range(ch, un+1):
                answer.append(matrix[te][i])
            te += 1
            for i in range(te, pa+1):
                answer.append(matrix[i][un])
            un -= 1
            if te <= pa:
                for i in range(un, ch-1, -1):
                    answer.append(matrix[pa][i])
                pa -= 1
            if ch <= un:
                for i in range(pa, te-1, -1):
                    answer.append(matrix[i][ch])
                ch += 1
        return answer
