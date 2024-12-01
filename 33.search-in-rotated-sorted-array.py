# @leet start


def find_diff(nums):
    if len(nums) == 1 or nums[0] < nums[-1]:
        return 0
    left, right = 0, len(nums) - 2
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] > nums[mid + 1]:
            return len(nums) - mid - 1
        if nums[mid] <= nums[left]:
            right = mid - 1
        else:
            left = mid + 1


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        diff = find_diff(nums)

        def transform(oi):
            return (len(nums) + oi - diff) % len(nums)

        def value(oi):
            return nums[transform(oi)]

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if value(mid) == target:
                return transform(mid)
            if value(mid) > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1


# @leet end

