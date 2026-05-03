class Solution:
    def climbStairs(self, n: int) -> int:
        count=0
        for steps in range(1,(n//2)+1):
            count+=(n-1)//steps
        return count+1
