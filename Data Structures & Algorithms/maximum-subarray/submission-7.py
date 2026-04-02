class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        sub = nums[0]

        for i in range(1, len(nums)):
            if sub < 0:
                sub = 0
            
            sub += nums[i]
            res = max(sub, res)
        return res