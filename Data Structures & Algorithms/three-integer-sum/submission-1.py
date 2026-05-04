class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        left=0
        right=len(nums)-1
        ans=[]
        odd_step=1
        while right-left>=3:
            sum_of_first_last=nums[left]+nums[right]
            if (-1*sum_of_first_last) in nums[left+1:right-1]:
                ans.append(sorted([nums[left],nums.index((-1*sum_of_first_last)),nums[right]]))
            if odd_step:
                left+=1
                odd_step=0
            else:
                right-=1
                odd_step=1
        return ans
