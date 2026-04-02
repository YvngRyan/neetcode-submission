class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        prevStep, currStep = 1, 2

        for i in range(2, n):
            temp = currStep
            currStep = prevStep + currStep
            prevStep = temp
        return currStep