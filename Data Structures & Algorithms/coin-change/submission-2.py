class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [[amount + 1] * (amount + 1) for _ in range(len(coins))]

        # Single cell in dp table = Given all the options of coins up to index r (row),
        # The value in the cell is the minimum amount of coins to reach that amount

        for r in range(len(coins)):
            dp[r][0] = 0

        for c in range(amount + 1):
            if c >= coins[0]:
                dp[0][c] = 1 + dp[0][c - coins[0]]

        for r in range(1, len(coins)):
            for c in range(amount + 1):
                skip = dp[r - 1][c]

                include = amount + 1
                if c >= coins[r]:
                    include = dp[r][c - coins[r]] + 1
                dp[r][c] = min(skip, include)
        return dp[len(coins) - 1][amount] if dp[len(coins) - 1][amount] <= amount else -1