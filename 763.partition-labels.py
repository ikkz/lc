# @leet start
from collections import defaultdict

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ranges = dict()
        for i, c in enumerate(s):
            if c in ranges:
                ranges[c][1] = i
            else:
                ranges[c] = [i, i] 
        res = []
        ranges = sorted(ranges.values())
        s, e = ranges[0]
        for start, end in ranges[1:]:
            if start > e:
                res.append(e - s + 1)
                s, e = start, end
            else:
                e = max(e, end)
        res.append(e - s + 1)
        return res




# @leet end
