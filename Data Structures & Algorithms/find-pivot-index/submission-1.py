class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = [0] * len(nums)
        postfix = [0] * len(nums)

        prefixSum = 0
        for i in range(len(nums)):
            prefixSum += nums[i]
            prefix[i] = prefixSum
        
        postfixSum = 0
        for i in range(len(nums) - 1, -1, -1):
            postfixSum += nums[i]
            postfix[i] = postfixSum
        
        for i in range(len(nums)):
            leftSum = None
            rightSum = None
            if i == 0:
                leftSum = 0
            else:
                leftSum = prefix[i - 1]

            if i != len(nums) - 1:
                rightSum = postfix[i + 1]
            else:
                rightSum = 0
            
            if leftSum == rightSum:
                return i
        return -1