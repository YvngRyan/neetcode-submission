class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [0] * (len(t) + 1)
        dp[len(t)] = 1

        for r in range(len(s) - 1, -1, -1):
            newDp = [0] * (len(t) + 1)
            newDp[len(t)] = 1
            for c in range(len(t) - 1, -1, -1):
                if s[r] == t[c]:
                    newDp[c] += dp[c + 1] + dp[c]
                else:
                    newDp[c] += dp[c]
            dp = newDp
        return dp[0]