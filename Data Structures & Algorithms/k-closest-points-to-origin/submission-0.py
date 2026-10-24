class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        q = []
        dist = 0
        for i in range(len(points)):
            x, y = points[i]
            dist = (x)**2 + (y)**2
            heapq.heappush(q, [-dist, [x, y]])
            if len(q)>k:
                heapq.heappop(q)
        return [point for _, point in q]
        
