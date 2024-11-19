from typing import List


# @leet start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        def move_right():
            last = nums[-1]
            for i in range(len(nums) - 1, 0, -1):
                nums[i] = nums[i - 1]
            nums[0] = last

        def move_left():
            first = nums[0]
            for i in range(0, len(nums) - 1):
                nums[i] = nums[i + 1]
            nums[-1] = first

        k = k % len(nums)
        if k < len(nums) - k:
            while k:
                move_right()
                k -= 1
        else:
            k = len(nums) - k
            while k:
                move_left()
                k -= 1

    def _rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def reverse(i, j):
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        k = k % len(nums)
        reverse(len(nums) - k, len(nums) - 1)
        reverse(0, len(nums) - k - 1)
        reverse(0, len(nums) - 1)


# @leet end

