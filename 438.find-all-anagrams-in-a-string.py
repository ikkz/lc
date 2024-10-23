from typing import List
# @leet start


def bucket(s: str) -> List[int]:
    buk = [0] * 26
    for c in s:
        buk[ord(c) - ord("a")] += 1
    return buk


def add(a: List[int], b: List[int]) -> List[int]:
    return list(ax + bx for (ax, bx) in zip(a, b))


def sub(a: List[int], b: List[int]) -> List[int]:
    return list(ax - bx for (ax, bx) in zip(a, b))


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        target = bucket(p)
        wnd = bucket(s[: len(p)])
        l, r = 0, len(p) - 1
        res = []
        while True:
            if wnd == target:
                res.append(l)
            wnd[ord(s[l]) - 97] -= 1
            l += 1
            r += 1
            if r < len(s):
                wnd[ord(s[r]) - 97] += 1
            else:
                break
        return res

    def _findAnagrams(self, s: str, p: str) -> List[int]:
        buckets = [bucket("")]
        for i in range(len(s)):
            buckets.append(add(buckets[-1], bucket(s[i : i + 1])))
        target = bucket(p)
        res = []
        for i, (a, b) in enumerate(zip(buckets, buckets[len(p) :])):
            if sub(b, a) == target:
                res.append(i)
        return res


# @leet end
