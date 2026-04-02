class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0

        l = 0
        for r in range(len(prices)):
            prof = prices[r] - prices[l]
            res = max(prof, res)

            if prices[r] < prices[l]:
                l = r
        return res