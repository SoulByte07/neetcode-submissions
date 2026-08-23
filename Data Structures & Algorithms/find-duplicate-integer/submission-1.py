class Solution:
    def findDuplicate(self, n: List[int]) -> int:
        si,fi=0,0
        sv,fv=n[si],n[fi]
        while True:
            si=n[sv]
            sv=n[si]
            fi=n[sv]
            fv=n[fi]
            if sv==fv:
                return n[si]