class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = [0] * len(nums)
        postfix = [0] * len(nums)

        currPrefix = 0
        for i in range(len(nums)):
            prefix[i] = currPrefix
            currPrefix += nums[i]

        currPostfix = 0
        for i in range(len(nums) - 1, -1, -1):
            postfix[i] = currPostfix
            currPostfix += nums[i]
        
        for i in range(len(nums)):
            if postfix[i] == prefix[i]:
                return i
        return -1