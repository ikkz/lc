# @leet start
class Solution:
    def rob(self, nums: List[int]) -> int:
        tou, butou = nums[0], 0
        for k in nums[1:]:
            tou, butou = k + butou, max(tou, butou)
        return max(tou, butou)


# @leet end

