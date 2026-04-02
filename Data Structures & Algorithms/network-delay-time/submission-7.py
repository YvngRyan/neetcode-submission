class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = { node : [] for node in range(1, n + 1)}
        for src, tgt, ti in times:
            adjList[src].append((tgt, ti))
        
        visit = set()
        visit.add(k)
        minHeap = []

        for tgt, ti in adjList[k]:
            minHeap.append((ti, tgt))
        
        heapq.heapify(minHeap)
        
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

        # adjList: { 1: [(2, 1), (4, 4)], 2: [(3, 1)], 3: [(4, 1)], 4: []}
        # visit : { 1, 2, 3, 4 }
        # res = 3
        # minHeap = [(4, 4)]

        # (4, 3)
