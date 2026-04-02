class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []

        preProd = 1
        for n in nums:
            res.append(preProd)
            preProd *= n
        
        postProd = 1
        for i in range(len(res) - 1, -1, -1):
            res[i] *= postProd
            postProd *= nums[i]
        
        return res