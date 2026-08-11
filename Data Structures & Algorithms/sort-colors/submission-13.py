class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0, 0, 0]

        for n in nums:
            count[n] += 1
        
        i = 0
        for n in range(0, 3):
            for cnt in range(count[n]):
                nums[i] = n
                i += 1
        return nums