class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cache = {}
        def search(index, flag):
            if index >= len(nums):
                return 0 if flag else float("-inf")
            
            if (index, 1) in cache:
                return cache[(index, 1)]
            
            if flag:
                cache[(index, 1)] = max(0, nums[index] + search(index + 1, True))
            else:
                cache[(index, 0)] = max(search(index + 1, False), nums[index] + search(index + 1, True))
            
            if flag:
                return cache[(index, 1)]
            else:
                return cache[(index, 0)]
        
        return search(0, False)