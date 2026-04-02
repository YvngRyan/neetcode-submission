class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def search(index, flag):
            if index >= len(nums):
                return 0 if flag else float("-inf")
            
            if flag:
                return max(0, nums[index] + search(index + 1, True))
            
            return max(search(index + 1, False), nums[index] + search(index + 1, True))
        
        return search(0, False)