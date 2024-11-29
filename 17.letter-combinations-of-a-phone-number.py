# @leet start

ALPHA = [
    "abc",
    "def",
    "ghi",
    "jkl",
    "mno",
    "pqrs",
    "tuv",
    "wxyz"
]

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res = [""]
        for c in digits:
            digit = ALPHA[ord(c) - ord('2')]
            next = []
            for p in res:
                for a in digit:
                    next.append(p + a)
            res = next
        return res

# @leet end
