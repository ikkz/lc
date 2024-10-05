from typing import List


# @leet start


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        low, high = 1, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            mid_count, low_count, high_count = 0, 0, 0
            for i in nums:
                if low <= i < mid:
                    low_count += 1
                elif mid < i <= high:
                    high_count += 1
                elif i == mid:
                    mid_count += 1
            if mid_count > 1:
                return mid
            elif low_count > mid - low:
                high = mid - 1
            else:
                low = mid + 1
        return -1


# @leet end

