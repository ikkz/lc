# @leet start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1] * (n + 1) for n in range(numRows)]
        for n in range(2, numRows):
            for k in range(1, n + 1):
                res[n][k] = sum(res[n - 1][k - 1 : k + 1])
        return res


# @leet end

