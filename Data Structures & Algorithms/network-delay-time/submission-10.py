class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = { node: [] for node in range(1, n + 1) }

        for src, tgt, ti in times:
            adjList[src].append((ti, tgt))
        
        minHeap = [(0, k)]
        visit = set()

        while minHeap:
            ti, node = heapq.heappop(minHeap)
            visit.add(node)

            if len(visit) == n:
                return ti

            for neiTi, nei in adjList[node]:
                if nei not in visit:
                    heapq.heappush(minHeap, (ti + neiTi, nei))
        return -1
                