# @leet start
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            dp[i][0] = int(text1[i] == text2[0])
        for j in range(n):
            dp[0][j] = int(text1[0] == text2[j])
        for i in range(m):
            for j in range(n):
                cand = [dp[i][j]]
                if i > 0:
                    cand.append(dp[i - 1][j])
                if j > 0:
                    cand.append(dp[i][j - 1])
                if i > 0 and j > 0:
                    cand.append(dp[i - 1][j - 1] + 1 if text1[i] == text2[j] else dp[i - 1][j - 1])
                if cand:
                    dp[i][j] = max(cand)
        return dp[m - 1][n - 1]

# @leet end
