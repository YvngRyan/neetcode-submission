class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        seen = set()

        def dfs(row, col):
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or (row, col) in seen or grid[row][col] == "0":
                return
            
            seen.add((row, col))
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r, c) not in seen and grid[r][c] == "1":
                    dfs(r, c)
                    res += 1
        return res