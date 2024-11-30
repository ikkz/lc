# @leet start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def bt(current, left, right):
            if left > right:
                return
            if left == 0 and right == 0:
                res.append(current)
                return
            if left > 0:
                bt(current + '(', left - 1, right)
            if right > left:
                bt(current + ')', left, right - 1)
        bt('', n, n)
        return res

# @leet end
