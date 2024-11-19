from typing import List


# @leet start
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]

        swaped = True
        cnt = 0
        while swaped:
            cnt += 1
            swaped = False
            for i, k in enumerate(nums):
                target = k - 1
                if (
                    i != target
                    and target >= 0
                    and target < len(nums)
                    and nums[target] - 1 != target
                ):
                    swap(i, target)
                    swaped = True
        for i, k in enumerate(nums):
            if i != k - 1:
                return i + 1
        return len(nums) + 1


# @leet end

