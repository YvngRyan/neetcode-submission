class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        sub = nums[0]

        for i in range(1, len(nums)):
            sub = max(sub + nums[i], nums[i])
            res = max(sub, res)
        return res