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