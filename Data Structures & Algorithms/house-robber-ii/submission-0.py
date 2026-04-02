class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums):
        cache = {}
        def dfs(i):
            if i in cache:
                return cache[i]
            if i >= len(nums):
                return 0
            
            cache[i] = max(nums[i] + dfs(i + 2), dfs(i + 1))
            return cache[i]
        return dfs(0)