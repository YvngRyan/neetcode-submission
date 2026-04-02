class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        dp[len(s1)][len(s2)] = True

        for r in range(len(s1), -1, -1):
            for c in range(len(s2), -1, -1):
                if r < len(s1) and s1[r] == s3[r + c] and c < len(s2) and s2[c] == s3[r + c]:
                    dp[r][c] = dp[r + 1][c] or dp[r][c + 1]
                elif r < len(s1) and s1[r] == s3[r + c]:
                    dp[r][c] = dp[r + 1][c]
                elif c < len(s2) and s2[c] == s3[r + c]:
                    dp[r][c] = dp[r][c + 1]
        return dp[0][0]
                

        # cache = {}
        # def dfs(s1Idx, s2Idx):
        #     if (s1Idx, s2Idx) in cache:
        #         return cache[(s1Idx, s2Idx)]
        #     if s1Idx + s2Idx == len(s3):
        #         return s1Idx == len(s1) and s2Idx == len(s2)

        #     cache[(s1Idx, s2Idx)] = False
        #     if s1Idx < len(s1) and s1[s1Idx] == s3[s1Idx + s2Idx] and s2Idx < len(s2) and s2[s2Idx] == s3[s1Idx + s2Idx]:
        #         cache[(s1Idx, s2Idx)] = dfs(s1Idx + 1, s2Idx) or dfs(s1Idx, s2Idx + 1)
        #     elif s1Idx < len(s1) and s1[s1Idx] == s3[s1Idx + s2Idx]:
        #         cache[(s1Idx, s2Idx)] = dfs(s1Idx + 1, s2Idx)
        #     elif s2Idx < len(s2) and s2[s2Idx] == s3[s1Idx + s2Idx]:
        #         cache[(s1Idx, s2Idx)] =  dfs(s1Idx, s2Idx + 1)
            
        #     return cache[(s1Idx, s2Idx)]
            
        # return dfs(0, 0)