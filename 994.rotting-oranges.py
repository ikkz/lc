# @leet start
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        time = [[None] * n for _ in range(m)]
        mt = 0

        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    time[i][j] = -1
                    q.append((i, j))
        while q:
            i, j = q.popleft()
            t = time[i][j]
            mt = max(mt, t + 1)
            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                ni, nj = i + di, j + dj 
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1 and time[ni][nj] is None:
                    time[ni][nj] = t + 1
                    grid[ni][nj] = 2
                    q.append((ni, nj))

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        return mt

# @leet end
