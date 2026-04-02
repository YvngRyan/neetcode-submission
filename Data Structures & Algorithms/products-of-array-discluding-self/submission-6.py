class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixPostfix = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            prefixPostfix[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            prefixPostfix[i] *= postfix
            postfix *= nums[i]
        
        return prefixPostfix