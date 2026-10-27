class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxRes = float('-inf')
        maxSeen = float('-inf')
        sum = 0
        for i in range(len(nums)):
            val = nums[i]
            maxSeen = max(maxSeen, val)
            if sum+val<0:
                maxRes = max(maxRes, sum)
                sum = 0
                continue
            sum += val
            maxRes = max(maxRes, sum)

        if maxRes==0:
            return maxSeen
        else:
            return maxRes


            
