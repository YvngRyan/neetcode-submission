class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        capHeap = []
        profHeap = []

        for i in range(len(profits)):
            capHeap.append((capital[i], profits[i]))
        
        heapq.heapify(capHeap)
        while k > 0 and (capHeap or profHeap):
            while capHeap and capHeap[0][0] <= w:
                cap, prof = heapq.heappop(capHeap)
                heapq.heappush(profHeap, -prof)
            if profHeap:
                w += -heapq.heappop(profHeap)
            k -= 1
        return w