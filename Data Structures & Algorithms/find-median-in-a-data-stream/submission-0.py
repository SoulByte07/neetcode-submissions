class MedianFinder:

    def __init__(self):
        self.minHeap = []


    def addNum(self, num: int) -> None:
        heapq.heappush(self.minHeap, num)
        

    def findMedian(self) -> float:
        if len(self.minHeap)%2!=0:
            return self.minHeap[len(self.minHeap)//2]
        else:
            mean = (self.minHeap[(len(self.minHeap)//2)-1] + self.minHeap[len(self.minHeap)//2])/2
            return mean
        
        