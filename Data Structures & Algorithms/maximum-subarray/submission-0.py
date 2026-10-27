class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        maxRes = float('-inf')
        sum = 0
        for i in range(len(nums)):
            val = nums[i]
            if sum+val<0:
                maxRes = max(maxRes, sum)
                maxRes = max(maxRes, val)
                sum = 0
                continue
            sum += val
            maxRes = max(maxRes, sum)
        return sum


            
