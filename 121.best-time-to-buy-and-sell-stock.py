# @leet start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pmin = prices[0]
        res = 0
        for n in prices[1:]:
            res = max(res, n - pmin)
            pmin = min(pmin, n)
        return res
# @leet end
