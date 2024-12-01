# @leet start
class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        map = {"}": "{", ")": "(", "]": "["}
        for c in s:
            if c in '({[':
                    st.append(c)
            elif not st or st[-1] != map[c]:
                return False
            else:
                st.pop()
        return not st

# @leet end

