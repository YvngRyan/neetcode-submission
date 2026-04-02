class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [0] * (len(word2) + 1)
        for c in range(len(word2) + 1):
            dp[c] = len(word2) - c

        for r in range(len(word1) - 1, -1, -1):
            newDp = [0] * (len(word2) + 1)
            newDp[-1] = len(word1) - r
            for c in range(len(word2) - 1, -1, -1):
                if word1[r] == word2[c]:
                    newDp[c] = dp[c + 1]
                else:
                    newDp[c] = 1 + min(dp[c], newDp[c + 1], dp[c + 1])
            dp = newDp
        return dp[0]