class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        n = len(profit)
        def dfs(i, currCap):
            if i == n or currCap <= 0:
                return 0
            
            maxProf = dfs(i + 1, currCap)

            if currCap >= weight[i]:
                maxProf = max(maxProf, profit[i] + dfs(i, currCap - weight[i]))
            
            return maxProf
        
        return dfs(0, capacity)