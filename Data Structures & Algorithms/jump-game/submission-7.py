class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * len(nums)
        dp[-1] = True
        for i in range(len(nums) - 2, -1, -1):
            for j in range(nums[i] + 1):
                if (i + j) < len(dp) and dp[i + j] == True:
                    dp[i] = True
                    break
        return dp[0]
        # # Bottom Up
        # cache = {}
        # def jump(i):
        #     if i in cache:
        #         return cache[i]
        #     if i == len(nums) - 1:
        #         return True
            
        #     if i >= len(nums) or nums[i] == 0:
        #         return False
            
        #     cache[i] = False

        #     for j in range(nums[i] + 1):
        #         if jump(i + j):
        #             cache[i] = True
        #             break
            
        #     return cache[i]
        # return jump(0)