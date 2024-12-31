# @leet start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [([0] * n) for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        ml = (1, s[0])
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                if s[i] != s[j]:
                    dp[i][j] = False
                elif i + 1 > j - 1:
                    dp[i][j] = True
                else:
                    dp[i][j] = dp[i + 1][j - 1]
                if dp[i][j]:
                    ml = max(ml, (j - i + 1, s[i: j + 1]))
        return ml[1]

# @leet end
