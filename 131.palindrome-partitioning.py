# @leet start
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        mat = [[False] * n for _ in range(n)]
        for i in range(n):
            mat[i][i] = True
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if i + 1 == j:
                    mat[i][j] = s[i] == s[j]
                else:
                    mat[i][j] = mat[i + 1][j - 1] if s[i] == s[j] else False
        res = []

        def bt(start, acc):
            if start == len(s):
                res.append(acc.copy())
                return
            for j in range(start, n):
                if mat[start][j]:
                    acc.append(s[start : j + 1])
                    bt(j + 1, acc)
                    acc.pop()

        bt(0, [])
        return res


# @leet end

