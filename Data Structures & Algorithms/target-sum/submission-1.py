class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = [ defaultdict(int) for _ in range(len(nums) + 1)]

        dp[0][0] = 1

        for i in range(len(nums)):
            num = nums[i]
            for currSum, count in dp[i].items():
                dp[i + 1][currSum + num] += count
                dp[i + 1][currSum - num] += count
        return dp[len(nums)][target]