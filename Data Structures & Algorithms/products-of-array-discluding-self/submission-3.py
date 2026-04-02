class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        curr = 1

        for i in range(len(nums)):
            res[i] = curr
            curr *= nums[i]
        
        post = 1
        for i in range(len(nums) -1, -1, -1):
            res[i] *= post
            post *= nums[i]
        return res