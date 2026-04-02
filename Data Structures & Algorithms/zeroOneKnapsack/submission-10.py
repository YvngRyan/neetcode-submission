class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        cache = {}
        def dfs(i, cap):
            if (i, cap) in cache:
                return cache[(i, cap)]
            if i == len(profit):
                return 0
            
            cache[(i, cap)] = dfs(i + 1, cap)

            if cap >= weight[i]:
                p2 = profit[i] + dfs(i + 1, cap - weight[i])
                cache[(i, cap)] = max(cache[(i, cap)], p2)
            return cache[(i, cap)]
        return dfs(0, capacity)