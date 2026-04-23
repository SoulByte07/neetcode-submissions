class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=collections.Counter(nums)
        sorted_freq=list(sorted(freq.items(), key=lambda pair: pair[1], reverse=True))
        ans=[key for key,val in sorted_freq[:k]]
        return ans