class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l, r = 0, 0

        while r < len(nums):
            while r < len(nums) and nums[r] == val:
                r += 1
            if r < len(nums):
                nums[l] = nums[r]
                l += 1
                r += 1
        return l