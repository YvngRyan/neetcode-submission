class Solution:
    def rob(self, nums: List[int]) -> int:
        currMax = 0
        dp = {}
        def search(i):
            if i >= len(nums):
                return 0

            if i in dp:
                return dp[i]
            
            dp[i] = max(search(i + 1), nums[i] + search(i + 2))
            
            return dp[i]
        
        return search(0)