# @leet start
class Solution:
    def jump(self, nums: List[int]) -> int:
        rm, end, count = 0, 0, 0
        for i, k in enumerate(nums[:-1]):
            rm = max(rm, i + k)
            if i == end:
                end = rm
                count += 1
        return count
# @leet end
