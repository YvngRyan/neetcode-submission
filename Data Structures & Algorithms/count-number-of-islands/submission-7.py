class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, columns = len(grid), len(grid[0])
        seen = set()
        islands = 0

        def dfs(row, column):
            if row >= rows or column >= columns or row < 0 or column < 0 or grid[row][column] == "0" or (row, column) in seen:
                return
            
            seen.add((row, column))
            dfs(row + 1, column)
            dfs(row - 1, column)
            dfs(row, column + 1)
            dfs(row, column - 1)


        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == "1" and (r, c) not in seen:
                    dfs(r, c)
                    islands += 1
        return islands