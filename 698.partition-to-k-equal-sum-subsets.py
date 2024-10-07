from typing import List

# @leet start
import builtins


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        sum = builtins.sum(nums)
        if sum % k != 0:
            return False
        target = sum / k
        bucket = [0] * k

        def dfs(idx: int) -> bool:
            if idx == len(nums):
                return True
            for i in range(k):
                if i > 0 and bucket[i] == bucket[i - 1]:
                    continue
                if bucket[i] + nums[idx] <= target:
                    bucket[i] += nums[idx]
                    if dfs(idx + 1):
                        return True
                    bucket[i] -= nums[idx]
            return False

        return dfs(0)


# @leet end
