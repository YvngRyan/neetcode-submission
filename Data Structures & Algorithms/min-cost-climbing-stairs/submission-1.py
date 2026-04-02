class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = {}
        def climb(i):
            if i >= len(cost):
                return 0
            if i in cache:
                return cache[i]
            
            currCost = cost[i] if i >= 0 else 0
            cache[i] =  currCost + min(climb(i + 1), climb(i + 2))
            return cache[i]
        return climb(-1)