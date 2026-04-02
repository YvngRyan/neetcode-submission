class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        dp = [0] * (amount + 1)
        dp[0] = 1

        for r in range(len(coins) - 1, -1, -1):
            newDp = [0] * (amount + 1)
            newDp[0] = 1
            for c in range(amount + 1):
                if c >= coins[r]:
                    newDp[c] = dp[c] + newDp[c - coins[r]]
            dp = newDp
        return dp[amount]


        # Top Down
        # cache = {}
        # def dfs(i, total):
        #     if (i, total) in cache:
        #         return cache[(i, total)]
        #     if total == amount:
        #         return 1
        #     if i == len(coins) or total > amount:
        #         return 0

        #     cache[(i, total)] = (dfs(i + 1, total) + dfs(i, total + coins[i]))
        #     return cache[(i, total)]
        # return dfs(0, 0)