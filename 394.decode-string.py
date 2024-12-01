# @leet start
from io import StringIO

class Solution:
    def decodeString(self, s: str) -> str:
        st = [(1, StringIO())]
        i = 0
        while i < len(s):
            if s[i].isalpha():
                st[-1][1].write(s[i])
                i += 1
            elif s[i].isnumeric():
                end = s.index('[', i)
                st.append((int(s[i:end]), StringIO()))
                i = end + 1
            elif s[i] == ']':
                count, buf = st.pop()
                value = buf.getvalue()
                while count:
                    count -= 1
                    st[-1][1].write(value)
                i += 1
            else:
                assert False
        return st[-1][1].getvalue()


        

# @leet end
