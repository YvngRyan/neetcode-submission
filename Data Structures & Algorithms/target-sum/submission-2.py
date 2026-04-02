class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)

        dp[0] = 1

        for i in range(len(nums)):
            num = nums[i]
            newDp = defaultdict(int)
            for currSum, count in dp.items():
                newDp[currSum + num] += count
                newDp[currSum - num] += count
            dp = newDp
        return dp[target]