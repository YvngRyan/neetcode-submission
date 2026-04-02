class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        
        for c in range(amount + 1):
            if c >= coins[0]:
                dp[c] = 1 + dp[c - coins[0]]
            
        for r in range(1, len(coins)):
            newDp = [amount + 1] * (amount + 1)
            newDp[0] = 0
            for c in range(1, amount + 1):
                skip = dp[c]

                include = amount + 1
                if c >= coins[r]:
                    include = 1 + newDp[c - coins[r]]
                newDp[c] = min(skip, include)
            dp = newDp
        return dp[-1] if dp[-1] < (amount + 1) else -1