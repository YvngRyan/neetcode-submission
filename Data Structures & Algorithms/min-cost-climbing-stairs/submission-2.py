class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [-1] * (len(cost) + 1)
        dp[-1] = 0
        for i in range(len(cost) - 1, -1, -1):
            climb2 = dp[i + 2] if i + 2 < len(dp) else float('inf')
            climb1 = dp[i + 1] if i + 1 < len(dp) else float('inf')

            dp[i] = cost[i] + min(climb2, climb1)
        return min(dp[0], dp[1])


        # # Top down DP
        # cache = {}
        # def climb(i):
        #     if i >= len(cost):
        #         return 0
        #     if i in cache:
        #         return cache[i]
            
        #     currCost = cost[i] if i >= 0 else 0
        #     cache[i] =  currCost + min(climb(i + 1), climb(i + 2))
        #     return cache[i]
        # return climb(-1)