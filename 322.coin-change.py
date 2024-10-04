from typing import List


# @leet start
from itertools import chain


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            if coin <= amount:
                dp[coin] = 1
        for i in range(1, amount + 1):
            dp[i] = min(
                chain(
                    (
                        count + 1
                        for coin in coins
                        if i - coin >= 0 and (count := dp[i - coin]) != -1
                    ),
                    [dp[i]] if dp[i] != -1 else [],
                ),
                default=dp[i],
            )

        return dp[-1]


# @leet end
