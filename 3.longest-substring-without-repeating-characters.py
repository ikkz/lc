# @leet start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not len(s):
            return 0
        l, r = 0, 0
        cs = set(s[:1])
        m = 1
        while l < len(s):
            while r + 1 < len(s) and s[r + 1] not in cs:
                r += 1
                cs.add(s[r])
            m = max(m, r - l + 1)
            l += 1
            cs.remove(s[l - 1])
        return m


# @leet end

