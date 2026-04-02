class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}

        def climb(step):
            if step == n:
                return 1
            if step > n:
                return 0

            if step in cache:
                return cache[step]
            
            cache[step] = climb(step + 1) + climb(step + 2)
            
            return cache[step]
        return climb(0)