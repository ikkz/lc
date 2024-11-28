from typing import List

# @leet start
from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        def bfs(i, j):
            nonlocal visited
            q = deque()
            q.append((i, j))
            while q:
                i, j = q.popleft()
                visited[i][j] = True

                for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    ni, nj = i + di, j + dj 
                    if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == '1' and not visited[ni][nj]:
                        q.append((ni, nj))
                        visited[ni][nj] = True

        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not visited[i][j]:
                    bfs(i, j)
                    count += 1
        return count

# @leet end
