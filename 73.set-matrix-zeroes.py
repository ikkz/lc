# @leet start
class Solution:
    def setZeroes(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[i][j] = None
        for i in range(m):
            for j in range(n):
                if matrix[i][j] is None:
                    for k in range(m):
                        if matrix[k][j] is not None:
                            matrix[k][j] = 0
                    for k in range(n):
                        if matrix[i][k] is not None:
                            matrix[i][k] = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] is None:
                    matrix[i][j] = 0


# @leet end

