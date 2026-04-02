class Solution:
    def climbStairs(self, n: int) -> int:
        def climb(i):
            if i > n:
                return 0
            if i == n:
                return 1
            return climb(i + 1) + climb(i + 2)
            
        return climb(0)