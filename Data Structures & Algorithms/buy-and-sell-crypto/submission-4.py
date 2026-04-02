class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Brute Force
        maxProfit = 0
        for i in range(len(prices)):
            for j in range(i, len(prices), +1):
                profit = prices[j] - prices[i]
                maxProfit = max(profit, maxProfit)
        return maxProfit