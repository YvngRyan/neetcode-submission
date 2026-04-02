class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [0] * (len(text2) + 1)

        for r in range(len(text1) - 1, -1, -1):
            newDp = [0] * (len(text2) + 1)
            for c in range(len(text2) - 1, -1, -1):
                if text1[r] == text2[c]:
                    newDp[c] = 1 + dp[c + 1]
                else:
                    newDp[c] = max(dp[c], newDp[c + 1])
            dp = newDp
        return dp[0]