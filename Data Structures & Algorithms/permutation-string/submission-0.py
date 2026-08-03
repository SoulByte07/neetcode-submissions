class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq1=collections.Counter(s1)
        freq2=collections.Counter(s2)

        for k,v1 in freq1.items():
            if k not in freq2:
                return False
            if v1<freq2[k]:
                return False
        return True

