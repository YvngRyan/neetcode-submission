class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * (len(nums) + 2)

        for i in range(len(nums) -1, -1, -1):
            dp[i] = max(nums[i] + dp[i + 2], dp[i + 1])
        return dp[0]

        # # Top Down
        # cache = {}
        # def dfs(i):
        #     if i in cache:
        #         return cache[i]
        #     if i >= len(nums):
        #         return 0
            
        #     cache[i] = max(nums[i] + dfs(i + 2), dfs(i + 1))
        #     return cache[i]
        # return dfs(0)