# @leet start
from typing import List


def bucket(s: str) -> List[int]:
    bk = [0] * (ord("z") - ord("A") + 1)
    for c in s:
        bk[ord(c) - ord("A")] += 1
    return bk


def bk_add(bk, c):
    bk[ord(c) - ord("A")] += 1


def bk_del(bk, c):
    bk[ord(c) - ord("A")] -= 1


def bk_fit(bk1, bk2):
    for x, y in zip(bk1, bk2):
        if x < y:
            return False
    return True


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        bk_t = bucket(t)
        bk = bucket("")
        ms = None
        right = -1
        for left, c in enumerate(s):
            while right + 1 < len(s) and not bk_fit(bk, bk_t):
                right += 1
                bk_add(bk, s[right])
            if not bk_fit(bk, bk_t):
                break
            nm = (sum(bk), left, right)
            ms = min(ms, nm) if ms else nm
            bk_del(bk, c)
        return s[ms[1] : (ms[2] + 1)] if ms else ""


# @leet end

