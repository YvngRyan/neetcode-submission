class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        islands = 0

        def dfs(r, c):
            if r < 0 or r == ROWS or c < 0 or c == COLS or (r, c) in visit or grid[r][c] == "0":
                return
            
            visit.add((r, c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                dfs(nr, nc)


        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1" and (row, col) not in visit:
                    dfs(row, col)
                    islands += 1
        return islands
