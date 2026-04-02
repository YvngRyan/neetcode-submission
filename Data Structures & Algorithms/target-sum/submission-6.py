class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)
        dp[target] = 1
        for r in range(len(nums) - 1, -1, -1):
            newDp = defaultdict(int)
            for num in dp:
                newDp[num - nums[r]] += dp[num]
                newDp[num + nums[r]] += dp[num]
            dp = newDp
        return dp[0]

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