from typing import List
# @leet start

from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mp = defaultdict(lambda: 0)
        mp[0] = 1
        pre, count = 0, 0
        for e in nums:
            pre += e
            if pre - k in mp:
                count += mp[pre - k]
            mp[pre] += 1

        return count


# @leet end
