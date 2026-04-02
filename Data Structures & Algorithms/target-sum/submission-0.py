class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}
        def dfs(i, currSum):
            if i == len(nums):
                if currSum == target:
                    return 1
                else:
                    return 0
            
            if (i, currSum) in cache:
                return cache[(i, currSum)]
            
            cache[(i, currSum)] = dfs(i + 1, currSum - nums[i]) + dfs(i + 1, currSum + nums[i])
            return cache[(i, currSum)]
        
        return dfs(0, 0)