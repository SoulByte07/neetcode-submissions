class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxRes = nums[0]
        sum = 0
        for n in nums:
            if sum<0:
                sum = 0
            sum+=n
            maxRes = max(maxRes, sum)
        return maxRes