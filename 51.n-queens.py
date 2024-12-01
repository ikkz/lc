# @leet start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [[False] * n for _ in range(n)]
        def check(i, j):
            for k in range(0, i):
                if board[k][j]:
                    return False
            x, y = i, j
            while 0 <= x < n and 0 <= y < n:
                if board[x][y]:
                    return False
                x -= 1
                y -= 1
            x, y = i, j
            while 0 <= x < n and 0 <= y < n:
                if board[x][y]:
                    return False
                x -= 1
                y += 1
            return True

        res = []
        def record():
            res.append(
                [
                    "".join(map(lambda b: 'Q' if b else '.', board[i]))
                    for i in range(n)
                ]
            )

        def bt(i):
            if i == n:
                record()

            for j in range(n):
                if check(i, j):
                    board[i][j] = True
                    bt(i + 1)
                    board[i][j] = False
        bt(0)
        return res
        
# @leet end
