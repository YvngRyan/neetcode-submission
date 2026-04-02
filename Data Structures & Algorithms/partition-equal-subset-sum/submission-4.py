class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False

        target = total // 2

        cache = {}

        def dfs(i, currSum):
            if currSum == target:
                return True
            if i == len(nums):
                return False

            if (i, currSum) in cache:
                return cache[(i, currSum)]
            
            cache[(i, currSum)] = dfs(i + 1, currSum + nums[i]) or dfs(i + 1, currSum)
            
            return cache[(i, currSum)]
        
        return dfs(0, 0)