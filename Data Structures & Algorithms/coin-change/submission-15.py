class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
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