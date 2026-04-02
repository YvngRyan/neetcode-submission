class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = defaultdict(list)

        for src, tgt, time in times:
            adjList[src].append((tgt, time))
        
        resList = {}
        minHeap = [(0, k)]

        while minHeap:
            currTime, currTgt = heapq.heappop(minHeap)

            if currTgt not in resList:
                resList[currTgt] = currTime
            
            for newTgt, newTime in adjList[currTgt]:
                if newTgt not in resList:
                    heapq.heappush(minHeap, (currTime + newTime, newTgt))
        
        res = 0
        for i in range(1, n + 1):
            if i not in resList:
                return -1
            res = max(res, resList[i])
        return res