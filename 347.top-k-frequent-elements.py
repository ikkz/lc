from typing import Dict, List

# @leet start

from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count: Dict[int, int] = defaultdict(int)
        for n in nums:
            count[n] += 1
        return list(
            map(
                lambda t: t[-1],
                sorted(
                    list(map(lambda t: tuple(reversed(t)), count.items())), reverse=True
                )[:k],
            )
        )


# @leet end

