from typing import List

# @leet start

from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            cs = [0] * 26
            for c in s:
                cs[ord(c) - ord("a")] += 1
            res[tuple(cs)].append(s)
        return list(res.values())


# @leet end

