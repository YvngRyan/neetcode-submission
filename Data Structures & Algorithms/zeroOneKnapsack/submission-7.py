class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        cache = {}
        def dfs(i, currCap):
            if (i, currCap) in cache:
                return cache[(i, currCap)]
            if currCap <= 0 or i == len(profit):
                return 0
            
            cache[(i, currCap)] = dfs(i + 1, currCap)

            if currCap >= weight[i]:
                cache[(i, currCap)] = max(cache[(i, currCap)], profit[i] + dfs(i + 1, currCap - weight[i]))
            
            return cache[(i, currCap)]
        
        return dfs(0, capacity)