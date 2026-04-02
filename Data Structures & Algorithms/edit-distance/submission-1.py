class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]
        for r in range(len(word1)):
            dp[r][-1] = len(word1) - r
        for c in range(len(word2)):
            dp[-1][c] = len(word2) - c
            
        for r in range(len(word1) - 1, -1, -1):
            for c in range(len(word2) - 1, -1, -1):
                if word1[r] == word2[c]:
                    dp[r][c] = dp[r + 1][c + 1]
                else:
                    dp[r][c] = 1 + min(dp[r + 1][c], dp[r][c + 1], dp[r + 1][c + 1])
        return dp[0][0]



        # DP (Top Down)
        # cache = {}
        # def dfs(w1Idx, w2Idx):
        #     if (w1Idx, w2Idx) in cache:
        #         return cache[(w1Idx, w2Idx)]
        #     if w2Idx == len(word2):
        #         return len(word1) - w1Idx  
        #     if w1Idx == len(word1):
        #         return len(word2) - w2Idx

        #     cache[(w1Idx, w2Idx)] = 0
        #     if word1[w1Idx] == word2[w2Idx]:
        #         cache[(w1Idx, w2Idx)] = dfs(w1Idx + 1, w2Idx + 1)
        #     else:
        #         # Delete (emulate), Insert (emulate), Replace
        #         cache[(w1Idx, w2Idx)] = min(1 + dfs(w1Idx + 1, w2Idx),
        #                     1 + dfs(w1Idx, w2Idx + 1),
        #                     1 + dfs(w1Idx + 1, w2Idx + 1))
        #     return cache[(w1Idx, w2Idx)]
            
        # return dfs(0, 0)