class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False

        target = total // 2

        def dfs(i, curr):
            if curr == 0:
                return True
            if i == len(nums):
                return False
            
            return dfs(i + 1, curr) or dfs(i + 1, curr - nums[i])
        
        return dfs(0, target)