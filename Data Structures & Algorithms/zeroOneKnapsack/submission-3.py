class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        n = len(profit)
        dp = [[0] * (capacity + 1) for _ in range(n)]

        for r in range(len(dp)):
            dp[r][0] = 0
        
        for c in range(len(dp[0])):
            if c >= weight[0]:
                dp[0][c] = profit[0]

        for r in range(1, len(dp)):
            for c in range(1, len(dp[0])):
                skip = dp[r - 1][c]

                include = 0
                if c >= weight[r]:
                    include = profit[r] + dp[r-1][c - weight[r]]
                
                dp[r][c] = max(include, skip)
        
        return dp[n - 1][capacity]