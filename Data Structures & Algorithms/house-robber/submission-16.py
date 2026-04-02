class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}
        def maxRob(i):
            if i >= len(nums):
                return 0
            
            if i in cache:
                return cache[i]
            
            cache[i] = max(nums[i] + maxRob(i + 2), maxRob(i + 1))
            
            return cache[i]
        return maxRob(0)