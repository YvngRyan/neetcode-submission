class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = { node : [] for node in range(1, n + 1)}
        for src, tgt, ti in times:
            adjList[src].append((tgt, ti))
        
        visit = set()
        minHeap = [(0, k)]
        
        res = 0
        while minHeap and len(visit) != n:
            ti, node = heapq.heappop(minHeap)
            if node in visit:
                continue
            res = ti
            visit.add(node)

            for tgt, ti2 in adjList[node]:
                if tgt not in visit:
                    heapq.heappush(minHeap, (ti + ti2, tgt))
        
        return res if len(visit) == n else -1