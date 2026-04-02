class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0

        l, r = 0, 0

        while r < len(prices) - 1:
            r += 1
            if prices[r] < prices[l]:
                l = r
            else:
                diff = prices[r] - prices[l]
                res = max(diff, res)
        return res