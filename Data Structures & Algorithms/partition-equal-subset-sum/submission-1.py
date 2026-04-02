class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        
        target = total // 2
    

        def dfs(i, target):
            if i == len(nums):
                return target == 0
            
            if target < 0:
                return False
            
            return dfs(i + 1, target - nums[i]) or dfs(i + 1, target)
        
        return dfs(0, target)