class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxB = max(piles)

        l, r = 1, maxB

        minRate = None

        while l <= r:
            m = (r + l) // 2
            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p) / m)
            if totalTime <= h:
                minRate = m
                r = m - 1
            else:
                l = m + 1
        
        return minRate