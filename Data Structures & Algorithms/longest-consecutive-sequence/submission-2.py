class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        res = 0

        for n in nums:
            curr = 1
            if n - 1 in numSet:
                continue
            else:
                while n + curr in numSet:
                    curr += 1
                res = max(res, curr)
        return res