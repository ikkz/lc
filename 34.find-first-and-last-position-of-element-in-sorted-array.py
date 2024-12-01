# @leet start

def find_start(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target and (mid == 0 or nums[mid - 1] < target):
            return mid
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def find_end(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target and (mid == len(nums) - 1 or nums[mid + 1] > target):
            return mid
        if nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = find_start(nums, target)
        return [start, -1 if start == -1 else find_end(nums, target)]

# @leet end
