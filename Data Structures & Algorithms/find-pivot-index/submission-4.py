class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sumLeft = [0] * len(nums)
        sumRight = [0] * len(nums)

        currSum = 0
        for i in range(len(nums)):
            sumLeft[i] = currSum
            currSum += nums[i]
        
        currSum = 0
        for i in range(len(nums) - 1, -1, -1):
            sumRight[i] = currSum
            currSum += nums[i]
        
        for i in range(len(nums)):
            if sumLeft[i] == sumRight[i]:
                return i
        return -1