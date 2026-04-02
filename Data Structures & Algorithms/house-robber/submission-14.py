class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return nums[0]
        
        rob1, rob2 = nums[0], max(nums[0], nums[1])
        i = 2
        while i < len(nums):
            tmp = rob2
            rob2 = max(rob2, nums[i] + rob1)
            rob1 = tmp
            i += 1
        return rob2