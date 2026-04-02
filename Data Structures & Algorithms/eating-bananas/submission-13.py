class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res = max(piles)

        l, r = 1, res

        while l <= r:
            m = (r + l) // 2

            time = 0

            for p in piles:
                time += math.ceil(p / m)
            
            if time > h:
                l = m + 1
            else:
                r = m - 1
                res = m
        return res