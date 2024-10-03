from typing import List


# @leet start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        m = 1
        st = set(nums)
        for n in st:
            if n - 1 in st:
                continue
            cm = 0
            while n in st:
                cm += 1
                n += 1
            m = max(m, cm)
        return m


# @leet end

