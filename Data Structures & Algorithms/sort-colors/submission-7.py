class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0] * 3

        for n in nums:
            count[n] += 1
        
        numsIndex = 0
        for i in range(len(count)):
            while count[i] > 0:
                nums[numsIndex] = i
                count[i] -= 1
                numsIndex += 1
        return nums