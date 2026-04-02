class MedianFinder:

    def __init__(self):
        self.maxHeap = []
        self.minHeap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxHeap, -num)

        if len(self.maxHeap) > len(self.minHeap) + 1:
            n = heapq.heappop(self.maxHeap) * -1
            heapq.heappush(self.minHeap, n)
        
        if len(self.maxHeap) > 0 and len(self.minHeap) > 0:
            if -self.maxHeap[0] > self.minHeap[0]:
                n1 = heapq.heappop(self.maxHeap) * -1
                n2 = heapq.heappop(self.minHeap) * -1
                heapq.heappush(self.maxHeap, n2)
                heapq.heappush(self.minHeap, n1)

    def findMedian(self) -> float:
        if len(self.maxHeap) == len(self.minHeap):
            return (-self.maxHeap[0] + self.minHeap[0]) / 2
        else:
            return -self.maxHeap[0]
        
        