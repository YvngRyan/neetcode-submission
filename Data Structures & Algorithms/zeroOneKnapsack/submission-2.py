class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        n = len(profit)
        cache = {}
        def dfs(i, currCap):
            if i == n:
                return 0

            if (i, currCap) in cache:
                return cache[(i, currCap)]
                
            maxProf = dfs(i + 1, currCap)

            if currCap - weight[i] >= 0:
                p = profit[i] + dfs(i + 1, currCap - weight[i])
                maxProf = max(maxProf, p)

            cache[(i, currCap)] = maxProf
            return cache[(i, currCap)]
        
        return dfs(0, capacity)