class Solution:
    def minWindow(self, s: str, t: str) -> str:
        mapT=collections.Counter(t)
        window={}
        have,need=0,len(mapT)
        res, resLen=[-1,-1],float('infinity')
        l=0

        for r in range(len(s)):
            ch=s[r]
            window[ch]=1+window.get(ch,0)
            if ch in mapT and mapT[ch]>=window[ch]:
                have+=1
            while have==need:
                window[s[l]]-=1
                l+=1
                if s[l] in mapT and mapT[s[l]]>=window[s[l]]:
                    if (r-l+1)<resLen:
                        resLen=(r-l+1)
                        res=[l,r]
                else:
                    have-=1
        return s[l:r+1] if resLen!=float('infinity') else ""
                
                



        
        








