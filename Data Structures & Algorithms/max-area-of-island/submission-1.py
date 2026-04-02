class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        maxArea = 0
        seen = set()

        def dfs(row, col):
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or (row, col) in seen or grid[row][col] == 0:
                return 0
            
            seen.add((row, col))
            total = 1
            for dx, dy in directions:
                total += dfs(row + dx, col + dy)
            return total

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r, c) not in seen and grid[r][c] == 1:
                    maxArea = max(maxArea, dfs(r, c))
        return maxArea