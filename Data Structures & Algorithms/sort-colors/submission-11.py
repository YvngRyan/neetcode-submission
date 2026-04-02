class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        colors = [0] * 3
        for n in nums:
            colors[n] += 1
        
        i = 0
        for j in range(3):
            while colors[j] > 0:
                nums[i] = j
                colors[j] -= 1
                i += 1