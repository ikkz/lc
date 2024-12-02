# @leet start
squares = [n * n for n in range(1, 101)]
class Solution:
    def numSquares(self, n: int) -> int:
        nums = [n for n in range(n + 1)]
        nums[1] = 1
        for i in range(n + 1):
            for s in squares:
                if i + s > n:
                    break
                nums[i + s] = min(nums[i + s], nums[i] + 1)
        return nums[n]




# @leet end
