class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adjList = defaultdict(list)

        for source, to, price in flights:
            adjList[source].append((price, to))
        
        visit = set()

        minHeap = [(0, src, 0)]
        while minHeap:
            price, curr, stops = heapq.heappop(minHeap)
            if stops > k + 1:
                continue
            if curr == dst:
                return price
            
            visit.add(curr)
            
            for neiPrice, nei in adjList[curr]:
                if nei not in visit:
                    heapq.heappush(minHeap, (price + neiPrice, nei, stops + 1))

        return -1