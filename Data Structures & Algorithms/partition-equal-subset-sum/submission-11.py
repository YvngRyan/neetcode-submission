class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        target = total // 2

        dp = [False] * (target + 1)
        dp[0] = True
        
        for r in range(len(nums) - 1, -1, -1):
            newDp = [False] * (target + 1)
            newDp[0] = True
            for c in range(target + 1):
                skip = dp[c]
                include = dp[c - nums[r]] if c - nums[r] >= 0 else False
                newDp[c] = skip or include
            dp = newDp
        return dp[-1]

        # Top Down
        # total = sum(nums)
        # if total % 2:
        #     return False
        # target = total // 2

        # cache = {}
        # def dfs(i, curr):
        #     if (i, curr) in cache:
        #         return cache[(i, curr)]
        #     if curr == 0:
        #         return True
        #     if i == len(nums):
        #         return False
            
        #     cache[(i, curr)] = dfs(i + 1, curr) or dfs(i + 1, curr - nums[i])
        #     return cache[(i, curr)]
        
        # return dfs(0, target)