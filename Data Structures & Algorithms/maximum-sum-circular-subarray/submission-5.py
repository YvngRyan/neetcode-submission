class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = 0
        minSub = nums[0]
        maxSub = nums[0]
        currMax, currMin = 0, 0

        for i in range(len(nums)):
            currMax = max(nums[i], currMax + nums[i])
            currMin = min(currMin + nums[i], nums[i])
            total += nums[i]
            minSub = min(minSub, currMin)
            maxSub = max(maxSub, currMax)
        
        return max(maxSub, total - minSub) if maxSub > 0 else maxSub