from itertools import permutations

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        perms_S1=[''.join(p) for p in permutations(s1, len(s1))]
        for e in perms_S1:
            if e in s2:
                return True
        else:
            return False

