class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]

        for r in range(len(s) + 1):
            dp[r][-1] = 1

        for r in range(len(s) - 1, -1, -1):
            for c in range(len(t) - 1, -1, -1):
                if s[r] == t[c]:
                    dp[r][c] += dp[r + 1][c + 1] + dp[r + 1][c]
                else:
                    dp[r][c] += dp[r + 1][c]
        return dp[0][0]
        
        
        

        # DP (Top Down)
        # cache = {}
        # def dfs(sIdx, tIdx):
        #     if tIdx == len(t):
        #         return 1
        #     if sIdx == len(s):
        #         return 0

        #     if (sIdx, tIdx) in cache:
        #         return cache[(sIdx, tIdx)]

        #     # Take this letter (if it matches the letter in "t")
        #     # Don't take this letter (even if it matches), and continue dfs
        #     cache[(sIdx, tIdx)] = 0
        #     if s[sIdx] == t[tIdx]:
        #         cache[(sIdx, tIdx)] += dfs(sIdx + 1, tIdx + 1) + dfs(sIdx + 1, tIdx)
        #     else:
        #         cache[(sIdx, tIdx)] += dfs(sIdx + 1, tIdx)
            
        #     return cache[(sIdx, tIdx)]
        
        # return dfs(0, 0)
