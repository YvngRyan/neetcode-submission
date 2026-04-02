class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        minHeap = [(grid[0][0], 0, 0)]

        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        visit = set()
        t = 0
        while minHeap:
            lvl, r, c = heapq.heappop(minHeap)
            t = max(t, lvl)
            if r == N - 1 and c == N - 1:
                return t
                
            visit.add((r, c))

            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if (nr, nc) not in visit and nr >= 0 and nr < N and nc >= 0 and nc < N:
                    heapq.heappush(minHeap, (grid[nr][nc], nr, nc))