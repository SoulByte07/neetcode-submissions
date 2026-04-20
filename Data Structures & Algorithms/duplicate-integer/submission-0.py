class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
       freq=collections.Counter(nums)
       if any(val>1 for val in freq.values()):
        return True
       else:
        return False  