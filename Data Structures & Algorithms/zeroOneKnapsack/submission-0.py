class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        n = len(profit)
        def dfs(i, currCap):
            if i == n:
                return 0
        
            # Skip
            maxProf = dfs(i + 1, currCap)

            # Include: Check if we have enough capacity, if so include
            
            currCap -= weight[i]
            if currCap >= 0:
                p = profit[i] + dfs(i + 1, currCap)
                maxProf = max(maxProf, p)

            return maxProf
        
        return dfs(0, capacity)