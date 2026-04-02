class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 0
        for i in range(n - 1, -1, -1):
            curr = 0
            if i + 2 <= n:
                curr += two
            if i + 1 <= n:
                curr += one
            two = one
            one = curr
        return one