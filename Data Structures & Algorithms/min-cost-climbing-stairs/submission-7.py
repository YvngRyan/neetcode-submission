class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        one, two = 0, 0
        for i in range(len(cost) - 1, -1, -1):
            curr = 0
            curr = cost[i] + min(one, two)
            two = one
            one = curr
        return min(one, two)


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