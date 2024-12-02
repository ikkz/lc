from typing import List


# @leet start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [None] * (amount + 1)
        dp[0] = 0
        for i in range(amount + 1):
            for coin in coins:
                if i - coin >= 0 and dp[i - coin] is not None:
                    dp[i] = min(dp[i], dp[i - coin] + 1) if dp[i] else dp[i-coin] + 1
        return -1 if dp[i] is None else dp[i]


# @leet end
