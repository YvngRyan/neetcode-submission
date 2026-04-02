class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        visit = set()

        def dfs(r, c):
            if r < 0 or r == len(grid) or c < 0 or c == len(grid[0]) or (r, c) in visit or grid[r][c] == "0":
                return
            
            visit.add((r, c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                dfs(nr, nc)

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r, c) not in visit and grid[r][c] == "1":
                    res += 1
                    dfs(r, c)
        return res