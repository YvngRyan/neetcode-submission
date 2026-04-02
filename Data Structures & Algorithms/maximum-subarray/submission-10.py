class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]

        currSub = 0
        for n in nums:
            currSub = max(n, currSub + n)
            res = max(currSub, res)
        return res