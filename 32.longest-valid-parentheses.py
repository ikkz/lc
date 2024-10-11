# @leet start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        dp = [0] * len(s)
        for i in range(len(dp)):
            if s[i] == ")" and i > 0:
                prev = dp[i - 1]
                if i - prev - 1 >= 0 and s[i - prev - 1] == "(":
                    dp[i] = prev + 2
                    if i - prev - 2 >= 0:
                        dp[i] += dp[i - prev - 2]
        return max(dp, default=0)


# @leet end

