class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        visit = set()
        adjList = { (x, y) : [] for x, y in points }

        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i, len(points)):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adjList[(x1, y1)].append((dist, x2, y2))
                adjList[(x2, y2)].append((dist, x1, y1))


        total = 0
        minHeap = [(0, points[0][0], points[0][1])]

        while minHeap:
            dist, x, y = heapq.heappop(minHeap)
            if (x, y) in visit:
                continue
            visit.add((x, y))

            total += dist

            for nDist, nX, nY in adjList[(x, y)]:
                if (nX, nY) not in visit:
                    heapq.heappush(minHeap, (nDist, nX, nY))
        return total