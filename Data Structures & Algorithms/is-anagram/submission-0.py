class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       freq1=collections.Counter(s) 
       freq2=collections.Counter(t) 

       if freq1==freq2:
        return True
       else:
        return False
    