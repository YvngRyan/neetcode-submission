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