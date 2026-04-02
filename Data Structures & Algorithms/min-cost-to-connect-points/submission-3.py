class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adjList = defaultdict(list)

        for i in range(len(points)):
            x, y = points[i]
            for j in range(i + 1, len(points)):
                x1, y1 = points[j]
                dist = abs(x - x1) + abs(y - y1)
                adjList[i].append((dist, j))
                adjList[j].append((dist, i))
        
        res = 0
        minHeap = [(0, 0)]
        visit = set()
        while len(visit) < len(points):
            dist, i = heapq.heappop(minHeap)
            if i in visit:
                continue
            
            visit.add(i)
            res += dist
            for neighborDist, neighbor in adjList[i]:
                if neighbor not in visit:
                    heapq.heappush(minHeap, (neighborDist, neighbor))
        return res