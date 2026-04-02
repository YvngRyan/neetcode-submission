class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [[amount + 1] * (amount + 1) for _ in range(len(coins))]
        for r in range(len(coins)):
            dp[r][0] = 0
        
        for c in range(amount + 1):
            if c >= coins[0]:
                dp[0][c] = 1 + dp[0][c - coins[0]]
            
        for r in range(1, len(coins)):
            for c in range(1, amount + 1):
                skip = dp[r - 1][c]

                include = amount + 1
                if c >= coins[r]:
                    include = 1 + dp[r][c - coins[r]]
                dp[r][c] = min(skip, include)
        return dp[-1][-1] if dp[-1][-1] < (amount + 1) else -1

        # Top Down
        cache = {}
        def dfs(i, total):
            if (i, total) in cache:
                return cache[(i, total)]
            if total == amount:
                return 0
            if total > amount or i == len(coins):
                return float('inf')

            cache[(i, total)] = min(dfs(i + 1, total), 1 + dfs(i, total + coins[i]))
            return cache[(i, total)]
        
        res = dfs(0, 0)
        return res if res != float('inf') else -1