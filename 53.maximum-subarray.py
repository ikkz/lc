from typing import List

# @leet start


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sums = [0]
        for k in nums:
            sums.append(k + sums[-1])
        mi = 0
        ma = nums[0]
        for k in sums[1:]:
            ma = max(ma, k - mi)
            mi = min(mi, k)
        return ma


# @leet end

