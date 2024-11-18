# @leet start
class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 1
        for _ in range(n):
            c = a + b
            a = b
            b = c
        return a


# @leet end

