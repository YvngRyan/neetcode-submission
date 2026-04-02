class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = defaultdict(list)

        for src, tgt, time in times:
            adjList[src].append((tgt, time))
        
        visit = set()
        t = 0
        minHeap = [(0, k)]

        while minHeap:
            currTime, currTgt = heapq.heappop(minHeap)

            if currTgt in visit:
                continue
            visit.add(currTgt)
            t = currTime
            
            for newTgt, newTime in adjList[currTgt]:
                if newTgt not in visit:
                    heapq.heappush(minHeap, (currTime + newTime, newTgt))
        
        return t if len(visit) == n else -1