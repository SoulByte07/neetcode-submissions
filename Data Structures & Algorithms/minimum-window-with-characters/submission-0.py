class Solution:
    def minWindow(self, s: str, t: str) -> str:
        st_in = -1
        end_in = -1
        count = 0
        for i, e in enumerate(s):
            if e in t and st_in == -1:
                st_in = i
                count += 1
            elif e in t and st_in != -1:
                end_in = i
                count += 1
        if count == len(t):
            return s[st_in : end_in + 1]
        return ""
