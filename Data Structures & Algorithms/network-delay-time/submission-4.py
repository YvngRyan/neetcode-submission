class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = defaultdict(list)
        for src, tgt, time in times:
            adjList[src].append((time, tgt))
        
        minHeap = [(0, k)]
        visit = set()
        res = 0

        while minHeap:
            t1, n1 = heapq.heappop(minHeap)
            if n1 in visit:
                continue

            visit.add(n1)
            res = t1

            if len(visit) == n:
                return res
            
            for t2, n2 in adjList[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap, (t2 + t1, n2))
        return -1