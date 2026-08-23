class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow,fast=0,0
        slow=nums[slow]
        fast=nums[slow]
        while slow!=fast:
            slow=nums[slow]
            fast=nums[slow]
        return nums[slow]
