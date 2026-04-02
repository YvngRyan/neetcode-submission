class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        def dfs(i, currCap):
            if currCap <= 0 or i == len(profit):
                return 0
            
            maxProf = dfs(i + 1, currCap)

            if currCap >= weight[i]:
                maxProf = max(maxProf, profit[i] + dfs(i + 1, currCap - weight[i]))
            
            return maxProf
        
        return dfs(0, capacity)
