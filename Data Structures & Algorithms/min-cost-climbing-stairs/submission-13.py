class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        one, two = 0, 0

        for i in range(len(cost) -1, -1, -1):
            tmp = one
            one = cost[i] + min(one, two)
            two = tmp
        return min(one, two)

        # dp = [0] * (len(cost) + 2)

        # for i in range(len(cost) - 1, -1, -1):
        #     dp[i] += cost[i] + min(dp[i + 1], dp[i + 2])
        # return min(dp[0], dp[1])


        # # Top Down
        # cache = {}
        # def dfs(i):
        #     if i in cache:
        #         return cache[i]
        #     if i >= len(cost):
        #         return 0
            
        #     cache[i] = cost[i] + min(dfs(i + 1), dfs(i + 2))
        #     return cache[i]
        
        # return min(dfs(0), dfs(1))