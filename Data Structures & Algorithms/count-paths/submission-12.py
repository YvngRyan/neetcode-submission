class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[m - 1][n - 1] = 1
        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                dp[r][c] += dp[r + 1][c] + dp[r][c + 1]
        return dp[0][0]

        # Top Down
        # for r in range()
        # cache = {}
        # def dfs(r, c):
        #     if (r, c) in cache:
        #         return cache[(r, c)]
        #     if r == (m - 1) and (c == n - 1):
        #         return 1
        #     if r >= m or c >= n:
        #         return 0
            
        #     cache[(r, c)] = dfs(r + 1, c) + dfs(r, c + 1)
        #     return cache[(r, c)]
        
        # return dfs(0, 0)