class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea=0
        stack=[]
        for i,h in enumerate(heights):
            start=i
            while stack and stack[-1]<h:
                index, h=stack.pop()
                maxArea=max(maxArea, h*(i-index))
                start=index
            stack.append([i,h])
        for i,h in stack:
            maxArea=max(maxArea, h*(len(heights)-i))
        return maxArea
        