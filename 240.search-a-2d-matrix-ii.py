from typing import List


# @leet start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        x, y = 0, n - 1
        while 0 <= x < m and 0 <= y < n:
            value = matrix[x][y]
            if value == target:
                return True
            if value < target:
                x += 1
            else:
                y -= 1
        return False


# @leet end

