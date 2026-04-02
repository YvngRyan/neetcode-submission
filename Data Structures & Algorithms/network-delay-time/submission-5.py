class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = { node : [] for node in range(1, n + 1)}

        for src, tgt, ti in times:
            adjList[src].append((ti, tgt))
        
        visited = set()
        minHeap = [(0, k)]
        total = 0

        while minHeap:
            time, node = heapq.heappop(minHeap)

            if node in visited:
                continue
            
            total = time
            visited.add(node)

            for ti, tgt in adjList[node]:
                heapq.heappush(minHeap, (time + ti, tgt))
        
        return total if len(visited) == n else -1