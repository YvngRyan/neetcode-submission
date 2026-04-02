class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        countNums = set(nums)

        res = 0
        for n in nums:
            if (n - 1) in countNums:
                continue
            
            currNum = n
            while currNum in countNums:
                currNum += 1
            res = max(currNum - n, res)
        return res