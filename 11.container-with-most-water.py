from typing import List


# @leet start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r, m = 0, len(height) - 1, 0
        m = (r - l) * min(height[l], height[r])
        while l < r:
            if height[l] > height[r] and r - 1 > l:
                r -= 1
            elif l + 1 < r:
                l += 1
            else:
                break
            m = max(m, (r - l) * min(height[l], height[r]))
        return m


# @leet end
