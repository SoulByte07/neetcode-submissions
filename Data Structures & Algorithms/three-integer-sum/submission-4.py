class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums=list(set(nums))
        nums.sort()
        left=0
        right=len(nums)-1
        ans=[]
        odd_step=1
        while right-left>=3:
            sum_of_first_last=nums[left]+nums[right]
            for k in range(left+1,right):
                if nums[k]==(-1*sum_of_first_last):
                    ans.append([nums[left],nums[k],nums[right]])
            if odd_step:
                left+=1
                odd_step=0
            else:
                right-=1
                odd_step=1
        return ans
