class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        seen = set()
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        def dfs(r, c):
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or (r, c) in seen or grid[r][c] == 0:
                return 0
            
            seen.add((r, c))
            area = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                area += dfs(nr, nc)
            
            return 1 + area
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r, c) not in seen and grid[r][c] == 1:
                    area = dfs(r, c)
                    res = max(res, area)
        return res
