# @leet start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * len(s)
        for i in range(len(s)):
            for word in wordDict:
                if i - len(word) + 1 >= 0 and s[i - len(word) + 1: i + 1] == word:
                    if i - len(word) + 1 == 0 or dp[i - len(word)]:
                        dp[i] = True
                        break
        return dp[-1]

# @leet end
