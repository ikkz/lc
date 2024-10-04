from typing import List


# @leet start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pivot = 0  # 之前的元素必须是全部非零
        for idx in range(len(nums)):
            if nums[idx]:
                nums[pivot], nums[idx] = nums[idx], nums[pivot]
                pivot += 1


# @leet end

