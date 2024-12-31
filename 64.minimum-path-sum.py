# @leet start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [0] * n
        dp[0] = grid[0][0]
        for i in range(m):
            for j in range(n):
                if i == 0:
                    if j > 0:
                        dp[j] = dp[j - 1] + grid[i][j]
                else:
                    dp[j] = grid[i][j] + (min(dp[j], dp[j - 1]) if j > 0 else dp[j])
        return dp[-1]

# @leet end
