class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
        for r in range(len(s) + 1):
            dp[r][-1] = 1
        
        for r in range(len(s) - 1, -1, -1):
            for c in range(len(t) - 1, -1, -1):
                if s[r] == t[c]:
                    dp[r][c] += dp[r + 1][c + 1]
                dp[r][c] += dp[r + 1][c]
        return dp[0][0]
        # # Top Down
        # cache = {}
        # def dfs(i, j):
        #     if (i, j) in cache:
        #         return cache[(i, j)]
        #     if j == len(t):
        #         return 1
        #     if i == len(s):
        #         return 0
            
        #     cache[(i, j)] = 0
        #     if s[i] == t[j]:
        #         cache[(i, j)] += dfs(i + 1, j + 1)
            
        #     cache[(i, j)] += dfs(i + 1, j)
        #     return cache[(i, j)]
        # return dfs(0, 0)