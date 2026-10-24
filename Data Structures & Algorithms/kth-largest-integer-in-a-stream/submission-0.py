import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.q = []
        self.k = k
        for i in range(len(nums)):
            heapq.heappush(self.q, nums[i])
        

    def add(self, val: int) -> int:
        heapq.heappush(self.q, val)
        return self.q[-self.k]

        
