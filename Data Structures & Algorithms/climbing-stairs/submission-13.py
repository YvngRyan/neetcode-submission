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























        # cache = {}

        # def climb(step):
        #     if step == n:
        #         return 1
        #     if step > n:
        #         return 0

        #     if step in cache:
        #         return cache[step]
            
        #     cache[step] = climb(step + 1) + climb(step + 2)

        #     return cache[step]
        # return climb(0)