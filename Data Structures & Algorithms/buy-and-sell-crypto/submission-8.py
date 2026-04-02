class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        l = 0
        r = 1

        res = 0
        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
                r = l + 1
            else:
                diff = prices[r] - prices[l]
                res = max(res, diff)
                r += 1
        return res
            
        