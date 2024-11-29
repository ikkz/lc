# @leet start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def back(acc):
            if len(acc) == len(nums):
                res.append(acc.copy())
                return
            for k in nums:
                if k not in acc:
                    acc.append(k)
                    back(acc)
                    acc.pop()
        back([])
        return res

            


# @leet end
