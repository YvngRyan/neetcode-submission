class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[-1] = 1
        for i in range(len(dp) - 2, -1, -1):
            two = dp[i + 2] if i + 2 < len(dp) else 0
            dp[i] = dp[i + 1] + two
        return dp[0]

        # # Top Down
        # cache = {}
        # def dfs(i):
        #     if i == n:
        #         return 1
        #     if i > n:
        #         return 0
            
        #     if i in cache:
        #         return cache[i]
            
        #     cache[i] = dfs(i + 1) + dfs(i + 2)
        #     return cache[i]
        # return dfs(0)