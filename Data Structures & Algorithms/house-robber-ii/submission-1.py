class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums):
        one, two = 0, 0
        for i in range(len(nums) -1, -1, -1):
            tmp = one
            one = max(nums[i] + two, one)
            two = tmp
        return one


        # # Top Down
        # cache = {}
        # def dfs(i):
        #     if i in cache:
        #         return cache[i]
        #     if i >= len(nums):
        #         return 0
            
        #     cache[i] = max(nums[i] + dfs(i + 2), dfs(i + 1))
        #     return cache[i]
        # return dfs(0)