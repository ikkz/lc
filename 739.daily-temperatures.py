# @leet start
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = [0]
        res = [0] * len(temperatures)
        i = 1
        while i < len(temperatures):
            while st and temperatures[i] > temperatures[st[-1]]:
                j = st.pop()
                res[j] = i - j
            st.append(i)
            i += 1
        return res


# @leet end

