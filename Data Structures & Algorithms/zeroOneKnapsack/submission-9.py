class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        def dfs(i, cap):
            if i == len(profit):
                return 0
            
            p1 = dfs(i + 1, cap)

            if cap >= weight[i]:
                p2 = profit[i] + dfs(i + 1, cap - weight[i])
                p1 = max(p1, p2)
            return p1
        return dfs(0, capacity)