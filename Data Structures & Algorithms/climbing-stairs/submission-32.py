class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[-1] = 1
        for i in range(len(dp) - 1, -1, -1):
            if i + 2 < len(dp):
                dp[i] += dp[i + 2]
            if i + 1 < len(dp):
                dp[i] += dp[i + 1]
        return dp[0]