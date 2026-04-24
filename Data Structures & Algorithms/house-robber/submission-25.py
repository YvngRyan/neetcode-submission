class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * (len(nums) + 3)
        for i in range(len(nums) - 1, -1, -1):
            dp[i] = max(dp[i + 1], nums[i] + dp[i + 2])
        return dp[0]

        # Top Down
        # cache = {}
        # def dfs(i):
        #     if i >= len(nums):
        #         return 0
        #     if i in cache:
        #         return cache[i]
            
        #     cache[i] = max(dfs(i + 1), nums[i] + dfs(i + 2))
        #     return cache[i]
        # return dfs(0)