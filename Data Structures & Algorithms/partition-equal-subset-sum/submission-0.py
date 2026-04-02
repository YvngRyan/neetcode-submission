class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        def dfs(i, currSum):
            if i == len(nums):
                return False
            
            if (total - currSum) == currSum:
                return True
            
            if dfs(i + 1, currSum + nums[i]):
                return True
            
            if dfs(i + 1, currSum):
                return True
            
            return False
        
        return dfs(0, 0)