class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[-1] = 1
        for i in range(len(dp) - 2, -1, -1):
            two = 0
            one = 0
            if i + 2 < len(dp):
                two = dp[i + 2]
            one = dp[i + 1]
            dp[i] = one + two
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