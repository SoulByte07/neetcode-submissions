class Solution:
    def trap(self, height: List[int]) -> int:
        l=0
        area=0
        for r in range(1,len(height)):
            if height[l]==0:
                l+=1
                continue
            if height[l]<=height[r] or r==len(height):
                length=min(height[l],height[r])
                width=r-l-1
                area+=(length*width)-(sum(height[l+1:r]))
                l=r
        return area