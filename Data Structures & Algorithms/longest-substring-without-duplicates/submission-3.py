class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dup=[]
        glb_max_len=0
        count=0
        for e in s:
            if e not in dup:
                dup.append(e)
            else:
                count=len(dup)
                glb_max_len=max(count,glb_max_len)
               # dup.clear()
                dup[:] = []        
                dup.append(e)
        
        glb_max_len=max(len(dup),glb_max_len)
        return glb_max_len

