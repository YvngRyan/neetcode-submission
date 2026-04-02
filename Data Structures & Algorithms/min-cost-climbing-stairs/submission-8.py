class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        one, two = 0, 0
        for i in range(len(cost) - 1, -1, -1):
            curr = 0
            curr = cost[i] + min(one, two)
            two = one
            one = curr
        return min(one, two)