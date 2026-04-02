class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        minHeap = [(0, points[0][0], points[0][1])]
        visit = set()
        res = 0

        while minHeap and len(visit) < len(points):
            dist, x, y = heapq.heappop(minHeap)
            if (x, y) in visit:
                continue
            
            res += dist
            visit.add((x, y))

            for x1, y1 in points:
                if (x1, y1) != (x, y) and (x1, y1) not in visit:
                    heapq.heappush(minHeap, ((abs(x - x1) + abs(y - y1)), x1, y1))
        
        return res