class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=collections.Counter(nums)
        ans=[]
        for key,val in freq.items():
            if val>=k:
                ans.append(key)
        if len(ans)==0:
            maxval=max(freq.values())
            ans=[key for key, v in freq.items() if v == maxval]
            return ans
        else:
            return ans