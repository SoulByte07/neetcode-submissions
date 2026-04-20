class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        premap={}
        for i in range(0,n):
            diffrence=target-nums[i]
            if nums[i] in premap:
                return [premap.get(nums[i]),i]
            else:
                premap[diffrence]=i