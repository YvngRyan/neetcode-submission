class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s) + 2)
        dp[len(s)] = 1
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            elif i + 1 < len(s) and int(s[i:i + 2]) <= 26:
                dp[i] = dp[i + 1] + dp[i + 2]
            else:
                dp[i] = dp[i + 1]
        return dp[0]

        # # Top Down
        # cache = {}
        # def dfs(i):
        #     if i in cache:
        #         return cache[i]
        #     if i == len(s):
        #         return 1
        #     if i > len(s) or s[i] == "0":
        #         return 0
            
        #     cache[i] = 0

        #     if i + 1 < len(s) and int(s[i:i + 2]) <= 26:
        #         cache[i] = dfs(i + 1) + dfs(i + 2)
        #     else:
        #         cache[i] = dfs(i + 1)
        #     return cache[i]
        
        # return dfs(0)