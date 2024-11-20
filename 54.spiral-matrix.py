from typing import List

# @leet start
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


class Solution:
    def spiralOrder(self, matrix) -> List[int]:
        m, n = len(matrix), len(matrix[0])

        def reach_wall(i, j, d):
            ni, nj = i + d[0], j + d[1]
            return not (0 <= ni < m and 0 <= nj < n and matrix[ni][nj] is not None)

        def reach_end(i, j):
            for d in DIRECTIONS:
                if not reach_wall(i, j, d):
                    return False
            return True

        i, j = 0, 0
        dir = 0
        res = [matrix[i][j]]
        matrix[i][j] = None
        while True:
            if reach_wall(i, j, DIRECTIONS[dir]):
                dir = (dir + 1) % len(DIRECTIONS)
            i, j = i + DIRECTIONS[dir][0], j + DIRECTIONS[dir][1]
            if 0 <= i < m and 0 <= j < n:
                res.append(matrix[i][j])
                matrix[i][j] = None
            if reach_end(i, j):
                break
        return res


# @leet end

