# @leet start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def select(i, selected):
            if i == len(nums):
                res.append(selected.copy())
                return
            select(i + 1, selected)
            selected.append(nums[i])
            select(i + 1, selected)
            selected.pop()
        select(0, [])
        return res
# @leet end
