class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        dp = [0] * (capacity + 1)
        for c in range(capacity + 1):
            if c >= weight[0]:
                dp[c] = profit[0]
        
        for r in range(1, len(profit)):
            newDp = [0] * (capacity + 1)
            for c in range(1, capacity + 1):
                skip = dp[c]

                if c >= weight[r]:
                    include = profit[r] + dp[c - weight[r]]
                    skip = max(skip, include)
                newDp[c] = skip
            dp = newDp
        return dp[-1]