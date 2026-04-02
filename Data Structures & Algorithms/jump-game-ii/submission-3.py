class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        l, r = 0, 0

        while r < len(nums) - 1:
            farthestJ = 0
            for i in range(l, r + 1):
                farthestJ = max(farthestJ, nums[i])
            
            l = r + 1
            r += farthestJ
            jumps += 1
        return jumps