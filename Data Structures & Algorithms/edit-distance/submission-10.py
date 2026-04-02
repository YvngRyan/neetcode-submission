class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [0] * (len(word2) + 1)
        for j in range(len(word2)):
            dp[j] = len(word2) - j
        for i in range(len(word1) - 1, -1, -1):
            newDp = [0] * (len(word2) + 1)
            newDp[-1] = len(word1) - i
            for j in range(len(word2) - 1, -1, -1):
                if word1[i] == word2[j]:
                    newDp[j] += dp[j + 1]
                else:
                    newDp[j] += 1 + min(newDp[j + 1], dp[j], dp[j + 1])
            dp = newDp
        return dp[0]

        # # Top Down
        # cache = {}
        # def dfs(i, j):
        #     if (i, j) in cache:
        #         return cache[(i, j)]
        #     if i == len(word1) and j == len(word2):
        #         return 0
        #     if i == len(word1):
        #         return len(word2) - j
        #     if j == len(word2):
        #         return len(word1) - i
            
        #     cache[(i, j)] = 0
        #     if word1[i] == word2[j]:
        #         cache[(i, j)] += dfs(i + 1, j + 1)
        #     else:
        #         cache[(i, j)] += 1 + min(dfs(i, j + 1), dfs(i + 1, j), dfs(i + 1, j + 1)) # Insert, delete, replace
        #     return cache[(i, j)]
        
        # return dfs(0, 0)