class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        whole_product = 1
        count_zeros=0
        for num in nums:
            if num == 0:
                count_zeros+=1
            else:
                whole_product *= num
        ans = []
        if count_zeros>1:
            return [0 for _ in nums]
        elif count_zeros==1:
            ans=[0]* len(nums)
            index_of_zero=nums.index(0)
            ans[index_of_zero]=whole_product
            return ans
        else:
            for num in nums:
                product_except_curr = int(whole_product / num)
                ans.append(product_except_curr)
        return ans