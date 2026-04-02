class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}
        def dfs(i, curr):
            if (i, curr) in cache:
                return cache[(i, curr)]
            if i == len(nums):
                if curr == target:
                    return 1
                return 0
            
            cache[(i, curr)] = dfs(i + 1, curr - nums[i]) + dfs(i + 1, curr + nums[i])
            return cache[(i, curr)]
        return dfs(0, 0)