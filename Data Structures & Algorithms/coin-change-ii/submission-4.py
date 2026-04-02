class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        dp = [[0] * (amount + 1) for _ in range(len(coins) + 1)]
        for r in range(len(coins) + 1):
            dp[r][0] = 1
        
        for r in range(len(coins) - 1, -1, -1):
            for c in range(amount + 1):
                if c >= coins[r]:
                    dp[r][c] = dp[r + 1][c]
                    dp[r][c] += dp[r][c - coins[r]]
        return dp[0][amount]


        # DP (Top Down)
        # cache = {}
        # def dfs(i, total):
        #     if (i, total) in cache:
        #         return cache[(i, total)]
        #     if total == amount:
        #         return 1
        #     if total > amount or i == len(coins):
        #         return 0
            
        #     cache[(i, total)] = (dfs(i + 1, total) + dfs(i, total + coins[i]))
        #     return cache[(i, total)]
        # return dfs(0, 0)