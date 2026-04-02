class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        prevStep, currStep = 1, 2

        i = 3
        while i <= n:
            tmp = currStep
            currStep = currStep + prevStep
            prevStep = tmp
            i += 1
        return currStep
        