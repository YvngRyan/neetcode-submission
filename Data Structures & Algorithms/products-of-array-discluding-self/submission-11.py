class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []

        preFix = 1
        for i in range(len(nums)):
            res.append(preFix)
            preFix *= nums[i]
        
        postFix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postFix
            postFix *= nums[i]
        return res