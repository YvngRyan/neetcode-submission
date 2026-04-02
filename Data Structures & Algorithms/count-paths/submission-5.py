class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ROWS, COLS = m - 1, n - 1
        cache = {}
        def dfs(r, c):
            if r == ROWS and c == COLS:
                return 1
            if r >= m or c >= n:
                return 0
            if (r, c) in cache:
                return cache[(r, c)]
            cache[(r, c)] = dfs(r + 1, c) + dfs(r, c + 1)
            return cache[(r, c)]
        return dfs(0, 0)