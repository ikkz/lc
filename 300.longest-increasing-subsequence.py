from typing import List


# @leet start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i, n in enumerate(nums):
            dp[i] = max(
                (k + 1 for j, k in enumerate(dp[0:i]) if nums[j] < n),
                default=dp[i],
            )
        return max(dp)


# @leet end

