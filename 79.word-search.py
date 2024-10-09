from typing import List


# @leet start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        visited = [[False] * n for _ in range(m)]

        def dfs(i: int, j: int, idx: int) -> bool:
            if idx == len(word):
                return True
            if (
                not (0 <= i < m and 0 <= j < n)
                or visited[i][j]
                or word[idx] != board[i][j]
            ):
                return False
            visited[i][j] = True
            for ni in range(-1, 2):
                for nj in range(-1, 2):
                    if abs(ni) + abs(nj) == 1 and dfs(i + ni, j + nj, idx + 1):
                        return True
            visited[i][j] = False
            return False

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False


# @leet end
