class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            jumps = nums[i]
            if i + jumps >= goal:
                goal = i
        
        return goal == 0