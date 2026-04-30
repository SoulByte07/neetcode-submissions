class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        prefix_target={}
        prefix_target={-1:0}
        res=[[]]
        for i in range(0,len(nums)-1):
            for j in range(i+1,len(nums)):
                curr_prefix_sum = nums[i]+nums[j]
                if curr_prefix_sum in prefix_target:
                    res.append([j,prefix_target[curr_prefix_sum]])
                else:
                    prefix_target[curr_prefix_sum]=[i,j]
        return res
