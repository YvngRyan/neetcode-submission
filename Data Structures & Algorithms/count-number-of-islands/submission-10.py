class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        def dfs(r, c):
            visit.add((r, c))

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and (nr, nc) not in visit and grid[nr][nc] == "1":
                    dfs(nr, nc)

        visit = set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r, c) not in visit and grid[r][c] == "1":
                    res += 1
                    dfs(r, c)
        return res