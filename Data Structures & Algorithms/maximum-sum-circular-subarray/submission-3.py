class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        totalMax, totalMin = nums[0], nums[0]

        curr = 0
        currMax = 0
        currMin = 0
        total = 0
        
        for n in nums:
            currMax = max(n, currMax + n)
            currMin = min(n, currMin + n)
            
            total += n
            totalMax = max(totalMax, currMax)
            totalMin = min(totalMin, currMin)
        
        return max(totalMax, total - totalMin) if total > 0 else totalMax