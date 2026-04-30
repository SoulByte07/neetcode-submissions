class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha_str= ''.join(ch.lower() for ch in s if ch.isalnum())
        l=0
        r=len(alpha_str)-1
        while l<r:
            if alpha_str[l]!=alpha_str[r]:
                return False
            l+=1
            r-=1
        else:
            return True