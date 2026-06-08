class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dup=[]
        glb_max_len=0
        count=0
        for e in s:
            if e not in dup:
                count+=1
                dup.append(e)
            else:
                glb_max_len=max(count,glb_max_len)
                count=0
               # dup.clear()
                dup[:] = []        
        
        glb_max_len=max(count,glb_max_len)
        return glb_max_len

