class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res =[]
        subset =[]
        nums.sort()
        def dfs(i):
            if i>=len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[i])
            dfs(i+1)
            ele = subset.pop()
            while i<len(nums)-1 and nums[i+1]==ele:
                i+=1
            dfs(i+1)
        dfs(0)
        return res
