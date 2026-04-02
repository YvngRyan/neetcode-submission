class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [float('inf')] * len(nums)
        dp[-1] = 0

        for i in range(len(nums) - 2, -1, -1):
            for j in range(nums[i] + 1):
                if (i + j) < len(nums):
                    dp[i] = min(dp[i], dp[i + j] + 1)
        return dp[0]


        # # Top Down
        # cache = {}
        # def dfs(i):
        #     if i in cache:
        #         return cache[i]
        #     if i == len(nums) - 1:
        #         return 0
            
        #     if i >= len(nums) or nums[i] == 0:
        #         return float('inf')
            
        #     cache[i] = float('inf')
        #     for j in range(nums[i] + 1):
        #         jumps = 1 + dfs(i + j)
        #         cache[i] = min(cache[i], jumps)
        #     return cache[i]
        # return dfs(0)