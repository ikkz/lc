# @leet start
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        hp = []
        for n in nums:
            heapq.heappush(hp, n)
            if len(hp) == k + 1:
                heapq.heappop(hp)
        return heapq.heappop(hp)


# @leet end
