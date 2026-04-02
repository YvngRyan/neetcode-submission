class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        h1 = nums[0]
        h2 = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            tmp = h2
            h2 = max(nums[i] + h1, h2)
            h1 = tmp
        return h2