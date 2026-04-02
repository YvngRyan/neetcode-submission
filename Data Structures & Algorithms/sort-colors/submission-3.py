class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0] * 3
        for i in range(len(nums)):
            count[nums[i]] += 1

        j = 0
        for i in range(len(count)):
            for n in range(count[i]):
                nums[j] = i
                j += 1
        return nums