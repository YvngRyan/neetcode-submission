class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache = {}
        def dfs(i, total):
            if (i, total) in cache:
                return cache[(i, total)]
            if total == amount:
                return 1
            if total > amount or i == len(coins):
                return 0
            
            cache[(i, total)] = (dfs(i + 1, total) + dfs(i, total + coins[i]))
            return cache[(i, total)]
        return dfs(0, 0)