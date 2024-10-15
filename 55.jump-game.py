from typing import List


# @leet start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        right = 0
        i = 0
        while i <= right:
            right = max(right, i + nums[i])
            if right >= len(nums) - 1:
                return True
            i += 1
        return right >= len(nums) - 1


# @leet end
