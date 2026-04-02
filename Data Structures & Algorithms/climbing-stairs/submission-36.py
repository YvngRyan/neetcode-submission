class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        dp = [0] * (n + 1)
        dp[-1], dp[-2] = 1, 1
        for i in range(len(dp) - 3, -1, -1):
            dp[i] = dp[i + 1] + dp[i + 2]
        return dp[0]

        # # Top Down
        # cache = {}
        # def dfs(i):
        #     if i in cache:
        #         return cache[i]
        #     if i == n:
        #         return 1
        #     if i > n:
        #         return 0
            
        #     cache[i] = dfs(i + 1) + dfs(i + 2)
        #     return cache[i]
        
        # return dfs(0)