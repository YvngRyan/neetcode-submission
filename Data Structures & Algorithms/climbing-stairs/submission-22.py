class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        prev1 = 1
        prev2 = 2
        for i in range(n - 3, -1, -1):
            tmp = prev2
            prev2 = prev1 + prev2
            prev1 = tmp

        return prev2