from typing import List


# @leet start
class Solution:
    def trap(self, height: List[int]) -> int:
        left_max, right_max = [0] * len(height), [0] * len(height)
        left_max[0] = height[0]
        right_max[-1] = height[-1]
        for i in range(1, len(height)):
            left_max[i] = max(left_max[i - 1], height[i])
        for i in range(len(height) - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])
        sum = 0
        for i, k in enumerate(height):
            sum += max(min(left_max[i], right_max[i]) - k, 0)
        return sum


# @leet end
