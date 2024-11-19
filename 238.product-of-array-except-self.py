from typing import List


# @leet start
from itertools import islice


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_product, suffix_product = [0] * len(nums), [0] * len(nums)
        prefix_product[0] = nums[0]
        suffix_product[-1] = nums[-1]
        for i, k in islice(enumerate(nums), 1, None):
            prefix_product[i] = prefix_product[i - 1] * k
        for i in range(len(nums) - 2, -1, -1):
            suffix_product[i] = suffix_product[i + 1] * nums[i]
        res = [0] * len(nums)
        for i in range(len(nums)):
            res[i] = (prefix_product[i - 1] if i else 1) * (
                suffix_product[i + 1] if i + 1 < len(nums) else 1
            )
        return res


# @leet end

