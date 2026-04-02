class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp = [0] * (len(nums) + 2)
        rob1, rob2 = 0, 0
        for i in range(len(nums) -1, -1, -1):
            tmp = max(nums[i] + rob2, rob1)
            rob2 = rob1
            rob1 = tmp
        return rob1

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
