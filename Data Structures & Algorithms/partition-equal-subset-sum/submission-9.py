class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        target = total // 2

        cache = {}
        def dfs(i, curr):
            if (i, curr) in cache:
                return cache[(i, curr)]
            if curr == 0:
                return True
            if i == len(nums):
                return False
            
            cache[(i, curr)] = dfs(i + 1, curr) or dfs(i + 1, curr - nums[i])
            return cache[(i, curr)]
        
        return dfs(0, target)