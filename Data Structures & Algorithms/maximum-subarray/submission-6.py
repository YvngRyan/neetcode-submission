class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        currSum = 0
        for r in range(len(nums)):
            if currSum < 0:
                currSum = 0
            currSum += nums[r]
            res = max(currSum, res)
        return res