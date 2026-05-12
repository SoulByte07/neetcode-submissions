class Solution:
    def maxArea(self, heights: List[int]) -> int:
        global_max=0
        right=len(heights)-1
        left=0
        flag=0
        while left<right:
            lenght=right-left
            width=min(heights[right],heights[left])
            current_capacity=lenght*width
            global_max=max(current_capacity,global_max)
            if flag:
                left+=1
                flag=1
            else:
                right-=1
                flag=0
        return global_max

