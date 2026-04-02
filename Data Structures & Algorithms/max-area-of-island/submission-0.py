class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, columns = len(grid), len(grid[0])
        maxArea = 0
        seen = set()

        def dfs(row, column):
            if row >= rows or row < 0 or column >= columns or column < 0 or (row, column) in seen or grid[row][column] == 0:
                return 0
            seen.add((row, column))

            return (1 + dfs(row + 1, column) + dfs(row - 1, column) + dfs(row, column + 1) + dfs(row, column - 1))
        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 1 and (r, c) not in seen:
                    maxArea = max(maxArea, dfs(r, c))
        return maxArea