class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxDiff = 0
        for i, price in enumerate(prices):
            for j in range(i, len(prices), 1):
                diff = prices[j] - price
                maxDiff = max(maxDiff, diff)
        return maxDiff




        