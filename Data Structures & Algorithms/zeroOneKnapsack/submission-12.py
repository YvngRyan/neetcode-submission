class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        dp = [[0] * (capacity + 1) for _ in range(len(profit))]
        for r in range(len(profit)):
            dp[r][0] = 0
        for c in range(capacity + 1):
            if c >= weight[0]:
                dp[0][c] = profit[0]

        for r in range(1, len(profit)):
            for c in range(1, capacity + 1):
                skip = dp[r - 1][c]

                if c >= weight[r]:
                    include = profit[r] + dp[r - 1][c - weight[r]]
                    skip = max(skip, include)
                dp[r][c] = skip
        return dp[-1][-1]

        # Top Down
        # cache = {}
        # def dfs(i, cap):
        #     if (i, cap) in cache:
        #         return cache[(i, cap)]
        #     if i == len(profit):
        #         return 0
            
        #     cache[(i, cap)] = dfs(i + 1, cap)

        #     if cap >= weight[i]:
        #         p2 = profit[i] + dfs(i + 1, cap - weight[i])
        #         cache[(i, cap)] = max(cache[(i, cap)], p2)
        #     return cache[(i, cap)]
        # return dfs(0, capacity)