class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r=0,0
        res=currMax=0
        while r<len(s):
            if s[r] not in s[l:r]:
                r+=1
                currMax+=1
            else:
                l+=1
                currMax=len(s[l:r])
            res=max(currMax,res)
        return res
