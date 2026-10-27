class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxRes = float('-inf')
        sum = 0
        for i in range(len(nums)):
            val = nums[i]
            if sum+val<0:
                maxRes = max(maxRes, sum)
                sum = 0
                continue
            sum += val
        return sum


            
