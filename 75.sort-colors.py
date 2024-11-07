from typing import List


# @leet start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        z, t = 0, len(nums) - 1
        for i, k in enumerate(nums):
            if i > t:
                break
            match k:
                case 0:
                    nums[i], nums[z] = nums[z], nums[i]
                    z += 1
                case 2:
                    while t >= 0 and nums[t] == 2:
                        t -= 1
                    if i > t:
                        break
                    nums[i], nums[t] = nums[t], nums[i]
                    t -= 1
                    if not nums[i]:
                        nums[i], nums[z] = nums[z], nums[i]
                        z += 1


# @leet end
