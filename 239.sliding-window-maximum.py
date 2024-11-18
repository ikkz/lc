from typing import List


# @leet start
import heapq
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        res = []
        for i in range(len(nums)):
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)
            while q and q[0] < i - k + 1:
                q.popleft()
            if i >= k - 1:
                res.append(nums[q[0]])
        return res

    def _maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        els = []
        res = []
        for i, e in enumerate(nums):
            if i < k - 1:
                heapq.heappush(els, (-e, i))
            else:
                heapq.heappush(els, (-e, i))
                while els[0][1] < i - k + 1:
                    heapq.heappop(els)
                res.append(-els[0][0])
        return res


# @leet end
