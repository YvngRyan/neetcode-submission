class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cache = {}
        def jump(i):
            if i in cache:
                return cache[i]
            if i == len(nums) - 1:
                return True
            
            if i >= len(nums) or nums[i] == 0:
                return False
            
            cache[i] = False

            for j in range(nums[i] + 1):
                if jump(i + j):
                    cache[i] = True
                    break
            
            return cache[i]
        return jump(0)