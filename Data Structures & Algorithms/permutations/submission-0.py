class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res =[]
        self.backtrack([], nums, [False]*len(nums))
        return self.res

    def backtrack(self,perms, nums, pick):
        if len(perms)==len(nums):
            self.res.append(perms[:])
            return
        for i in range(len(nums)):
            if not pick[i]:
                perms.append(nums[i])
                pick[i]=True
                self.backtrack(perms, nums, pick)
                perms.pop()
                pick[i]=False