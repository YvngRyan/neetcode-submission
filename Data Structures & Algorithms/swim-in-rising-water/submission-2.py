class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # Start from the top left
        # Create a min heap with the possible grid positions we can explore, sorted by the property of minimum elevation
        # If the elevation in the next heap item is <= the water level at time t, then explore
        # If not, increment the time by 1 until the next heap item is valid, and then continue exploring

        ROWS, COLS = len(grid), len(grid[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        minHeap = [(grid[0][0], 0, 0)]
        visit = set()
        visit.add((0, 0))
        t = 0
        while minHeap:
            elevation, row, col = heapq.heappop(minHeap)

            t = max(t, elevation)

            if row == ROWS - 1 and col == COLS - 1:
                return t
            
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if nr >= 0 and nr < ROWS and nc >= 0 and nc < COLS and (nr, nc) not in visit:
                    heapq.heappush(minHeap, (grid[nr][nc], nr, nc))
                    visit.add((nr, nc))
        return -1