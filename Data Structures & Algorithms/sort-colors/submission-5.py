class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, len(nums) - 1
        i = 0

        def switch(pointer1, pointer2):
            temp = nums[pointer1]
            nums[pointer1] = nums[pointer2]
            nums[pointer2] = temp

        while i <= r:
            if nums[i] == 0:
                switch(i, l)
                l += 1
            elif nums[i] == 2:
                switch(i, r)
                r -= 1
                i -= 1
            i += 1