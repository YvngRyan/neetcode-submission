class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        res = 0

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(r, c):
            nonlocal res, currArea
            if r < 0 or r == ROWS or c < 0 or c == COLS or (r, c) in visit or grid[r][c] == 0:
                return
            
            currArea += 1
            visit.add((r, c))
            res = max(currArea, res)

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                dfs(nr, nc)


        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1 and (row, col) not in visit:
                    currArea = 0
                    dfs(row, col)
        return res