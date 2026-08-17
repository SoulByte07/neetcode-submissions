class Solution:
    def computeEating(self, piles: List[int], k: int) -> int:
        sumPile=0
        for i,p in enumerate(piles):
            # currPile=round(p/k)
            currPile=(p + k - 1) // k
            sumPile+=currPile
        return sumPile

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low,high=1,sum(piles) # lower and upper bound
        minSumPile=high 
        res=float('infinity') # min k
        while low<=high:
            mid=low+((high-low)//2) 
            sumPile=self.computeEating(piles,mid)
            if sumPile>h: # invalid and move left
                low=mid+1
            else: # valid and move right
                res=min(res,mid) # get the mid or k
                minSumPile=min(minSumPile,sumPile) # get min
                high=mid-1 # move right
        return res

            