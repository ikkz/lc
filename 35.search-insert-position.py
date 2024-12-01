# @leet start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] >= target and (mid == 0 or nums[mid - 1] < target):
                return mid
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return len(nums)
# @leet end
