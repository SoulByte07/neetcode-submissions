class Solution:
    def search(self, nums: List[int], target: int) -> int:
        index=-1
        l,r=0,len(nums)-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:
                index=mid 
                return index
            elif nums[mid]>target:
                l=mid+1
            else:
                r=mid-1
        return index
