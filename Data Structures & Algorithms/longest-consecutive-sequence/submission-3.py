class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        res = 0
        for num in nums:
            count = 1
            if num - 1 in numSet:
                continue
            
            while num + count in numSet:
                count += 1
            res = max(count, res)
        return res
        