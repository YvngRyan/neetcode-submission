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