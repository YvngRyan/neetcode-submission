class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = [defaultdict(int) for _ in range(len(nums) + 1)]
        dp[-1][target] = 1
        for r in range(len(nums) - 1, -1, -1):
            for num in dp[r + 1]:
                dp[r][num - nums[r]] += dp[r + 1][num]
                dp[r][num + nums[r]] += dp[r + 1][num]
        return dp[0][0]

        # # Top Down
        # cache = {}
        # def dfs(i, curr):
        #     if (i, curr) in cache:
        #         return cache[(i, curr)]
        #     if i == len(nums):
        #         if curr == target:
        #             return 1
        #         return 0
            
        #     cache[(i, curr)] = dfs(i + 1, curr - nums[i]) + dfs(i + 1, curr + nums[i])
        #     return cache[(i, curr)]
        # return dfs(0, 0)