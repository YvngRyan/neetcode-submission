class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l, r = 0 ,0

        while r < len(nums):
            if nums[r] == val:
                r += 1
                continue
            nums[l] = nums[r]
            r += 1
            l += 1
        return l