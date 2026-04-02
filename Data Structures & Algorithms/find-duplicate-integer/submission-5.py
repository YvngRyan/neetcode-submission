class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Go through the list of nums
        # For the VAL at an index, you want set nums[VAL] to negative
        # While iterating through the list of nums, check to see
        # if nums[VAL] is negative, if it is, it means we have already seen this value
        for n in nums:
            idx = abs(n)
            if nums[idx] < 0:
                return idx
            nums[idx] *= -1
        return -1