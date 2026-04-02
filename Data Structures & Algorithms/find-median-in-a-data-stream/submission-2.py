class MedianFinder:

    def __init__(self):
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, num * -1)
        if (self.small and self.large and (self.small[0] * -1) > self.large[0]):
            num = heapq.heappop(self.small) * -1
            heapq.heappush(self.large, num)
        
        if len(self.small) > len(self.large) + 1:
            num = heapq.heappop(self.small) * -1
            heapq.heappush(self.large, num)
        
        if len(self.large) > len(self.small) + 1:
            num = heapq.heappop(self.large) * -1
            heapq.heappush(self.small, num)
        

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return self.small[0] * -1
        elif len(self.large) > len(self.small):
            return self.large[0]
        
        return ((self.small[0] * -1) + self.large[0]) / 2
        
        