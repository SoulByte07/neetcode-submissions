class MedianFinder:

    def __init__(self):
        self.minHeapLeft = []
        self.minHeapRight = []


    def addNum(self, num: int) -> None:
        if not self.minHeapLeft:
            heapq.heappush(self.minHeapLeft, num)
            return
        heapq.heappush(self.minHeapRight, num)
        if self.minHeapRight:
            minVal = heapq.heappop(self.minHeapRight)
            self.minHeapLeft.append(minVal)
        return
        

    def findMedian(self) -> float:
        if len(self.minHeapLeft) + len(self.minHeapRight) %2!=0:
            return self.minHeapLeft[-1]
        else:
            return (self.minHeapLeft[-1] + self.minHeapRight[0])/2
       