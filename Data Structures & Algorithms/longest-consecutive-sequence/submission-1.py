class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = set(nums)
        res = 0
        for num in nums:
            if num - 1 in count:
                continue
            length = 0
            while num + length in count:
                length += 1
                res = max(res, length)
        return res
