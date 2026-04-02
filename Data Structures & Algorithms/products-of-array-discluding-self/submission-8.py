class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = [0] * len(nums)

        currProd = 1
        for i, n in enumerate(nums):
            product[i] = currProd
            currProd *= n
        
        currProd = 1
        for i in range(len(nums) - 1, -1, -1):
            n = nums[i]
            product[i] *= currProd
            currProd *= n
        return product