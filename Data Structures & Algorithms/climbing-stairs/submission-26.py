class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2:
            return n
        
        s1 = 1
        s2 = 2

        i = 3
        while i <= n:
            tmp = s2
            s2 = s2 + s1
            s1 = tmp
            i += 1
        return s2