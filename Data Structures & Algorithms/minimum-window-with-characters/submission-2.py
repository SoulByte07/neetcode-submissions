class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=='':
            return ''
        mapT=collections.Counter(t)
        window={}
        have,need=0,len(mapT)
        res, resLen=[-1,-1],float('infinity')
        l=0

        for r in range(len(s)):
            ch=s[r]
            window[ch]=1+window.get(ch,0)
            if ch in mapT and mapT[ch]==window[ch]:
                have+=1
            while have==need:
                if (r-l+1)<resLen:
                    res=[l,r]
                    resLen=r-l+1
                window[s[l]]-=1
                if s[l] in mapT and window[s[l]] < mapT[s[l]]:
                    have-=1
                l+=1
        l,r=res

        return s[l:r+1] if resLen!=float('infinity') else ""
                
                



        
        








