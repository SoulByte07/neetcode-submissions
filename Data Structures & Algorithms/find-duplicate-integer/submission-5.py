class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow,fast=0,0
        slow=nums[slow]
        fast=nums[nums[fast]]
        while slow!=fast:
            slow=nums[slow]
            fast=nums[nums[fast]]
        return nums[fast]
